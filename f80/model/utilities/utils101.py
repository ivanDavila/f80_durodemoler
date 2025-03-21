import json
import math
import pickle

import cv2 as cv
import numpy as np
from queue import Queue

# Funciones Lambda
volume = lambda x: (4/3) * math.pi * x**3
calc_factor = lambda x, y: round(np.sum(x * y),3)

# Fuciones
def open_image(img_name:str, rot:bool=False) -> np.array:
    """
    Regresa una imagen de la libreria OpenCV v4.2
    De requerirse, la imagen es rotada 90 grados.

    Parámetros:
    -img_name: Ruta de la imagen a leer.
    -root: Flag que indica si es necesario el rotar la imagen.
    """
    src = cv.imread(img_name)
    if rot:
        src = cv.rotate(src, cv.ROTATE_90_CLOCKWISE)
    return src

def open_binary(src_name:str) -> np.array:
    """
    Leer y regresa el contenido de un fichero binario.

    Parámetros:
    -src_name: Ruta del fichero binario.
    """
    with open(src_name, 'rb') as file:
        data = pickle.load(file)
    return data

def rotate_contorus(contornos:np.array, largo:float):
    """
    Rota los contornos detectados para que coincidan con la imagen.

    Parámetros:
    -contornos: Arreglo de numpy a rotar.
    -largo: Dimensión de la imagen.
    """
    for cont in contornos:
        cont = np.squeeze(cont)
        for coord in cont:
            try:
                c0 = coord[0]
                c1 = coord[1]
                coord[0] = largo - c1
                coord[1] = c0
            except:
                pass
    return contornos

def draw_contornos(src:np.array, contornos:np.array, color:tuple):
    """
    Dibuja los contornos detectados en la imagen.

    Parámetros:
    -src: Imagen a dibujar los contornos.
    -contornos: Arreglo con los contornos.
    -color: Tupla RGB que referencia al color de los contrornos 0-255.
    """
    src = cv.drawContours(src, contornos, -1, color, 2)
    return src

def get_points_sizes(contornos:np.array, pxl_scale:float=1.0):
    """
    Regresa los centro de los contornos y las area que ocupan en mm^2.

    Parámetros:
    -contornos: Arreglo con los contornos.
    -pxl_scale: Proporción de area de un pixel a mm^2.
    """
    point_list = [0] * len(contornos)
    size_list = np.zeros(len(contornos))
    for c in range(len(contornos)):
        if cv.moments(contornos[c])["m00"] != 0:
            point_list[c] = int(cv.moments(contornos[c])['m10']/cv.moments(contornos[c])['m00']), int(cv.moments(contornos[c])['m01']/cv.moments(contornos[c])['m00'])
        else:
            point_list[c] = 0,0
        size_list[c] =cv.contourArea(contornos[c])
    return np.array(point_list), size_list*pxl_scale

def get_cumulative(diamlist:np.array, bins:int=18):
    """
    Regresa el porcentaje acumulado de la distribución granulométrica
    en base al volumen.

    Parámetros:
    -diamlist: Arreglo numpy con los diametros de las particulas detectadas.
    -bins: Numero de bins en los que se divide el histrograma de tamaños.
    """
    histvalues, histbase = np.histogram(diamlist, bins=bins)
    histbase_vol = np.array(list(map(volume, histbase/2)))
    histvalues_bin = histbase_vol[:-1] * histvalues / sum(histbase_vol[:-1] * histvalues) * 100

    histvalues_bin_2 = histbase_vol[:-1] * histvalues / sum(histbase_vol[:-1] * histvalues) * 86

    cumulative = np.cumsum(histvalues_bin)
    cumulative_2 = np.cumsum(histvalues_bin_2) + 14

    return histbase, cumulative, cumulative_2


def get_f(cumulative:np.array, histbase:np.array, cum:int):
    """
    Regresa el valor que representa el "cum %" de lo acumulado.

    Parámetros:
    -cumulative: Array de numpy con los porcentajes acumulados.
    -histbase: Array de numpy con los tamaños de la distribución.
    -cum: Porcentaje de acumulado del cual se desea el tamaño correspondiente.
    """
    index = np.where(cumulative > cum)[0][0] + 1
    f = histbase[index]
    return f, index

def count_size_bins(
    size_mm:np.array,
    point_list:np.array,
    ini:int, end:int, bins:int,
    f80:float, f50:float, f20:float):
    """
    Cuenta el numero de particulas por cada region de la imagen y las ordena
    segun el tamaño.

    Parámetros:
    -size_mm: Arreglo numpy con las dimensiones de las partículas.
    -point_list: Arreglo numpy con las posiciones del centro de los contornos.
    -ini, end, bins: Rango y numero de separaciones de las secciones de la imagen.
    -f80, f50, f20: Valores de los tamaños de partículas correnpodientes al f80, f50 y f20.
    """
    x_pos = [p[0] for p in point_list]
    y_pos = [p[1] for p in point_list]

    rango = np.linspace(ini, end, bins)
    gg = np.zeros(len(rango))
    gm = np.zeros(len(rango))
    fm = np.zeros(len(rango))
    ff = np.zeros(len(rango))

    for i, epoch in enumerate(rango):
        for size, x, y in zip(size_mm, x_pos, y_pos): # size_mm histbase
            if epoch+bins >= x > epoch:
                if size > f80:
                    gg[i] += 1
                elif size > f50:
                    gm[i] += 1
                elif size > f20:
                    fm[i] += 1
                else:
                    ff[i] += 1

    return gg, gm, fm, ff, x_pos, y_pos

def void_percent(image:np.array, nParts:int):
    """
    Caluclo de porcentaje de Vacio
    Input:
        imagen(np.array): Imagen BINARIA
        nParts: numero de partes en als que se desaea dividir la imagen
    """
    # img_rotate = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)
    im_height, im_width = image.shape
    # print(image.shape)

    #Conteo de pixeles de toda la imagen
    total_pxlZeroCount = len(image[image==0])
    total_Pxl = im_height * im_width

    # print("rec_height: %i" % im_height)
    # print("rec_width: %i" % im_width)

    # print("num de pixeles: %i" % total_pxlZeroCount)
    # print("numero total de pxl: %i" % total_Pxl)
    # print("proporcion Pxl Vacio: %0.2f" % (total_pxlZeroCount/total_Pxl))

    rec_lenght = int(im_width/nParts)
    void_prcnt = np.zeros(nParts)
    for i in range(nParts):
        rec_imag = image[0:, rec_lenght*i:rec_lenght*i + rec_lenght]
        # cv.imshow("hola2", rec_imag)
        # cv.waitKey(0)
        hei, wid = rec_imag.shape
        pxlZeroCount = len(rec_imag[rec_imag==0])
        void_prcnt_rec = pxlZeroCount/(hei*wid)
        # print(type(void_prcnt_rec))
        void_prcnt[i] = void_prcnt_rec

    return void_prcnt

#Vamos a crear un queue con perdida de datos
class myQueueu():
    def __init__(self, maxsize):
        self.myQueue = queue.Queue(maxsize=maxsize)
    
    def put(self, object):
        try:
            return self.myQueue.put(object, block=False)
        
        except queue.Full:
            self.myQueue.get()
            return self.myQueue.put(object,block=False)

    def get(self):
        return self.myQueue.get()

if __name__ == "__main__":
    
    image = cv.imread('imagensemantica.png', 0)
    
    ret,thresh1 = cv.threshold(image,127,255,cv.THRESH_BINARY)
    _2Darrayx = [range(0,10) for n in range(0,5)]

    print(type(image))

    nparray = np.array(_2Darrayx)
    print(nparray)
    vd_prcnt = void_percent(thresh1, 50)
    [print("void precent list: %s" % n) for n in vd_prcnt]
    
