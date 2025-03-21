import cv2
import configparser
import numpy as np
# import matplotlib.pyplot as plt
"""

imageUtilities1.05.py
Cambio de Output: anexo de mutilples Resultados puntuales en Cumulative

"""

class imageUtilities:
    def __init__(self, srcIm:np.array, configpath:str = "config.ini"):
        self.impart = 25
        self.iter=1
        self.configpath = configpath
        imagSize = self.readConfig()
        self.img = self.imgCrop(srcIm, imagSize)
    
    def readConfig(self):
        config = configparser.ConfigParser()
        config.read(self.configpath)
        str1 = config.get("myvars", "var1")
        r = tuple(map(int, str1.split(',')))
        return r
    
    def imgCrop(self, img, points:np.array):
        print(type(img))
        img_crop = img[points[1]:(points[1]+points[3]), points[0]:(points[0]+points[2])]
        return img_crop

    def cuadricula(self, segmentacion):
        imCrop_height = self.img.shape[0]
        imCrop_width = self.img.shape[1]
        for x in range(segmentacion):
            for y in range(segmentacion):
                imCrop_seg = self.img[int(imCrop_height/segmentacion*y):int(imCrop_height/segmentacion*y+imCrop_height/segmentacion),\
                int(imCrop_width/segmentacion*x):int(imCrop_width/segmentacion*x+imCrop_width/segmentacion)]
                yield imCrop_seg
    
    def cuadricula2(self, Sx, Sy, Si): # Sx -> Size x, Sy -> Size y, Si -> size intersection
        imCrop_height = self.img.shape[0]
        imCrop_width = self.img.shape[1]

        for x in range(int(imCrop_width/(Sx-Si))):
            for y in range(int(imCrop_height/(Sy-Si))):
                imCrop_seg = self.img[int((Sy - Si)*y):int((Sy - Si)*y+Sy),\
                int((Sx - Si)*x):int((Sx - Si)*x+Sx)]
                # print("image segmentations :[%i:%i, %i:%i]" % (int((Sy - Si)*y),int((Sy - Si)*y+Sy),int((Sx - Si)*x),int((Sx - Si)*x+Sx)))
                tupl = [imCrop_seg, int((Sx-Si)*x), int((Sy-Si)*y)]
                yield tupl
                
    def saveSegImage(self, imCrop_seg, dirname):
        for n in imCrop_seg:
            filename = dirname + "/image%i.png" % self.iter
            # cv2.imshow("hello", n)
            # cv2.waitKey(0)
            cv2.imwrite(filename, n)
            self.iter = self.iter + 1

    def saveImage(self, image, dirname):
        filename = dirname + "/image%i.png" % self.iter
        cv2.imwrite(filename, image)
        self.iter = self.iter + 1

    def bandDetector(self):
        imagBlur = cv2.resize(self.img, (int(self.img.shape[1]/2),int(self.img.shape[0]/2)))
        imagBlur = cv2.GaussianBlur(imagBlur,(15,15),cv2.BORDER_DEFAULT)
        return imagBlur
    
def cumulativeGraph(sizeList):
    # evaluate the histogram
    histvalues, histbase = np.histogram(sizeList, bins=20)

    # histbase_vol = np.array(list(map(volume, histbase/2)))

    # histvalues_bin = histbase_vol[:-1] * histvalues / sum(histbase_vol[:-1] * histvalues) * 100

    #evaluate the cumulativez
    cumulative = np.cumsum(histvalues)/len(sizeList)
    return histvalues, histbase, cumulative

def blobCharacteristcs(image):
    #Esta funcion solo es para imagen binarias
    kernel = np.ones((3,3),np.uint8)
    image = cv2.erode(image,kernel,iterations = 1)
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Inicializar Arreglos
    pointList = [None]*len(contours)
    sizeList = np.zeros(len(contours))
    for i in range(len(contours)):
        if cv2.moments(contours[i])['m00'] != 0:
            #Centroides de los contonrnos
            pointList[i] = int(cv2.moments(contours[i])['m10']/cv2.moments(contours[i])['m00']), int(cv2.moments(contours[i])['m01']/cv2.moments(contours[i])['m00'])
        else:
            pointList[i] = 0, 0
        #Areas de los contornos
        sizeList[i] = cv2.contourArea(contours[i])
    #Imagen Conttorno, centros de masa, areas
    return contours, pointList, sizeList

def drawLabels(image, pointList, sizeList):

    font = cv2.FONT_HERSHEY_SIMPLEX      # font 
    org = (0, 0)                        # org 
    fontScale = 1                       # fontScale 
    color = (255, 0, 0)                 # Blue color in BGR 
    thickness = 2                       # Line thickness of 2 px 

    image = cv2.putText(image, 'OpenCV', pointList[sizeList.argmax()], font,  
                fontScale, color, thickness, cv2.LINE_AA)

    return image

def enhanceImage(image, lookuptable):
    """Adjust contrast of an image.
    Args:
        imagen (numpy ndarray): numpy ndarray to be adjusted.
        lookuptable (numpy uint8): lookuptable
    Returns:
        numpy ndarray: Contrast adjusted image.
    """
    
    b, g, r = cv2.split(image)

    b = cv2.LUT(b, lookuptable)
    g = cv2.LUT(g, lookuptable)
    r = cv2.LUT(r, lookuptable)

    img_rslt = cv2.merge([b,g,r])
    return img_rslt

if __name__ == '__main__':
    segmntn = 6
    img = cv2.imread('data/Nacozari/200115/data 250ps/IMG200118_112205.BMP')
    xcon = imageUtilities(img)
    print("xcon: [%s,%s]" % (xcon.img.shape[0], xcon.img.shape[1]))

    for imgs in xcon.cuadricula2(250,250,50):
        print(imgs[0].shape)

    # xcon.saveSegImage(xcon.cuadricula(segmntn), "data/sample")
    # xcon2 = imageUtilities("data/Nacozari/200115/data 250ps/IMG200118_112206.BMP")
    # xcon2.iter = 36
    # xcon2.saveSegImage(xcon.cuadricula(segmntn), 'data/sample')s