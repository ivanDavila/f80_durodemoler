import numpy as np
import datetime

from cv2 import (imwrite, 
                 bitwise_and, 
                 bitwise_not, 
                 bitwise_or, 
                 countNonZero, 
                 cvtColor, 
                 drawContours, 
                 imencode, 
                 merge, 
                 flip, 
                 LUT, 
                 resize, 
                 rotate, 
                 split, 
                 COLOR_GRAY2RGB, 
                 COLOR_RGB2GRAY, 
                 IMWRITE_JPEG_QUALITY, 
                 INTER_AREA, 
                 INTER_CUBIC, 
                 ROTATE_90_CLOCKWISE, 
                 ROTATE_180, 
                 ROTATE_90_COUNTERCLOCKWISE
                 )
from math import sqrt
from math import pi as mathpi

from f80.model.utilities import *
# from utilities import *

from scipy.interpolate import interp1d

# from utilities import * #solo para prueba en __main__

pxlScale = 0.3955 #escalamiento en cerro lindo

def preprocess_image(source_img, configlist):
    try:
        #source_img = self.image[259:2741, :]
        height, width, _ = source_img.shape
        source_img = resize(source_img, (int(width/2),int(height/2)), INTER_CUBIC)

        #Cut imagen
        h, _, _= source_img.shape
        extract_image = source_img[
            h - configlist["ImgExtract_Point2"][1]:h - configlist["ImgExtract_Point1"][1],
            configlist["ImgExtract_Point1"][0]:configlist["ImgExtract_Point2"][0]]
        #Enhance Image
        if configlist['lookup_table_check']:
            lookup_table = np.array(configlist['lookup_table'], dtype=np.uint8)
            extract_image = enhanceImage(extract_image, lookup_table)

        #Rotate image            
        rotation_string = configlist['rotation']
        if rotation_string == '90':
            # print('Romsin-Rambler')
            image_rotate = rotate(extract_image, ROTATE_90_CLOCKWISE)

        elif rotation_string == '180':
            # print('Gaudin-Shuhmman')
            image_rotate = rotate(extract_image, ROTATE_180)

        elif rotation_string == '270':
            # print('Swebrec')
            image_rotate = rotate(extract_image, ROTATE_90_COUNTERCLOCKWISE)

        else:
            image_rotate = extract_image

        #Mirroring image
        if configlist['mirror']:
            preprocessed_image = flip(image_rotate, 1)
        else:
            preprocessed_image = image_rotate

        return preprocessed_image

    except Exception as e:
        print(e)
        print("Error: %s" % e)
        raise e

def smp_detection(source_img, configlist, model, progressBar = None):
    try:
        """
        Procesa la imagen
        """
        heigth_im, width_im, _ =  source_img.shape
        rect_coords = configlist['RectImages']
        #self.recImage = []
        if progressBar is not None:
            progressBar.setValue(0)

        num_image = len(rect_coords)
        # print("%s" % num_image)
        roca_detect_cmplta = np.zeros([heigth_im, width_im,3], dtype=np.uint8)
        count = 0

        #------------------------------Cambio F80ConfigPanl102.py-----------------------------------------------
        ROI_coord = [[rect_coords[0][0][0], rect_coords[0][0][1]],[rect_coords[-1][-1][0], rect_coords[-1][-1][1]]]
        print("ROI_coord: %s" % ROI_coord)
        Mask_ROI = roca_detect_cmplta.copy()
        Mask_ROI[ROI_coord[1][1]:ROI_coord[0][1],ROI_coord[0][0]:ROI_coord[1][0]] = 255
        bit_color = bitwise_and(source_img, Mask_ROI) #Imagen de granulometria Grande
        #--------------------------------------------------------------------------------------------------------

        for coords in rect_coords:
            points = coords
            point1 = points[0]
            point2 = points[1]

            # img_gray = cv.cvtColor(xcon.img, cv.COLOR_RGB2GRAY)
            recimage =  source_img[point2[1]:point1[1], point1[0]:point2[0]]
            #self.recImage.append(recimage)
            detect = model.Predictor(recimage)
            if detect.ndim > 2:
                roca_detect = detect[0]
            else:
                roca_detect = detect
                
            roca_detect[roca_detect==1] = 255
            roca_detectada_temp = np.zeros([heigth_im,width_im, 3], dtype=np.uint8)
            roca_detect_color = cvtColor(roca_detect, COLOR_GRAY2RGB)
            roca_detectada_temp[point2[1]:point1[1],point1[0]:point2[0]] =  roca_detect_color     
            roca_detect_cmplta = bitwise_or(roca_detect_cmplta, roca_detectada_temp)
            count = count + 1
            if progressBar is not None:
                processBar = int(100*count/num_image)
                progressBar.setValue(processBar)
        
        region_interes = roca_detect_cmplta[ROI_coord[1][1]:ROI_coord[0][1],ROI_coord[0][0]:ROI_coord[1][0]]
        region_interes = cvtColor(region_interes, COLOR_RGB2GRAY)

        #porcentaje de deteccion en region de interes
        ratio_rock = countNonZero(region_interes)/region_interes.size
        rockPercent = (ratio_rock * 100)

        roca_detect_cmplta_not = bitwise_not(roca_detect_cmplta)
        rock_detected_image = bitwise_and(source_img, roca_detect_cmplta) #Imagen de granulometria Grande
        not_rock_detected_image = bitwise_and(bit_color, roca_detect_cmplta_not) #Imagen de granulometria chica

        smp_detect_rslt = [rock_detected_image, not_rock_detected_image, roca_detect_cmplta, Mask_ROI]

        return smp_detect_rslt, rockPercent
    
    except Exception as e:
        print("Error: %s" % e)
        raise e
        
def segmentation(source_img, smp_detect_rslt, segmMin = False):
    try: 
        #------------------------------Cambio F80ConfigPanl102.py [inicio]-----------------------------------------------
        rock_detected_image, not_rock_detected_image, roca_detectada, Mask_ROI = smp_detect_rslt

        imgSegm_array =[]
        segmImag_max = segmentacionGrande(rock_detected_image, roca_detectada)
        img_Result = np.copy(source_img)

        countourn_max, centroidsList_max, sizeList_max = blobCharacteristcs(segmImag_max)
        color_max = (255, 0, 0)
        drawContours(img_Result, countourn_max, -1, color_max, 1)
        imgSegm_array.append(segmImag_max)

        if segmMin == True:
            segmImag_min = segmentacionMin(not_rock_detected_image, roca_detectada, Mask_ROI)
            countourn_min, centroidsList_min, sizeList_min = blobCharacteristcs(segmImag_min)
            color_min = (255, 0, 0)
            drawContours(img_Result, countourn_min, -1, color_min, 1)
            imgSegm_array.append(segmImag_min)
        #------------------------------Cambio F80ConfigPanl102.py [Fin]-----------------------------------------------

        return img_Result, segmImag_max, sizeList_max

        # self.SPD_toggled('Rosin-Rambler')

    except Exception as e:
        print("Error: %s" % e)
        raise e

def cumulative_graph(sizeList_min, pxlScale):
    try:
        diamList = []
        volList = []
        count = 0
        count_min_3mm = 0

        for area in sizeList_min:
            # print("area: %s" % type(area))
            real_area = area * pxlScale * pxlScale
            diam = sqrt(real_area)
            diamList.append(diam)
            vol = 1/8 * diam * diam * diam * 4/3 * mathpi
            volList.append(vol)
            count = count + 1
            if diam < 3:
                count_min_3mm = count_min_3mm + 1

        histbase, cumulative, _ = get_cumulative(diamList, 12)

        psd = interp1d(cumulative.tolist(), histbase[:-1].tolist())

        Fs = psd([10,20,30,40,50,60,70,80,90])

        Fs = np.append(Fs, max(histbase))

        data_result = [Fs, count, count_min_3mm]

        real_cumulative = [histbase, cumulative]

        diamList = np.array(diamList)

        diamDir = {
                "malla 1" : [diamList[diamList>25.4]],
                "malla 1/2" : [diamList[(diamList<25.4) & (diamList>12.7)]],
                "malla 3/8" : [diamList[(diamList<12.7) & (diamList>9.52)]],
                "malla 1/4" : [diamList[(diamList<9.52) & (diamList>6.35)]],
                "malla 4"   : [diamList[(diamList>6.35) & (diamList>4.75)]],
                "malla 6"   : [diamList[(diamList>4.75) & (diamList>3.35)]],
                "malla 10"  : [diamList[(diamList>3.35) & (diamList>2.36)]]
        }
        
        return real_cumulative, diamDir, data_result
    
    except Exception as e:
        print("Error: %s" % e)
        # raise e
    
    # except ValueError as e:
    #     print(e)

def mesh_graph(sizeList_min, pxlScale):

    opening = np.array([0, 38, 53, 75, 106, 150, 212, 300, 425, 600, 850, 1180, 
                1700, 2360, 3350, 4750, 6700, 9500, 12700, 19050, 25400])

    diamList = []
    volList = []
    count = 0
    count_min_3mm = 0

    for area in sizeList_min:
        # print("area: %s" % type(area))
        real_area = area * pxlScale * pxlScale
        diam = sqrt(real_area)
        diamList.append(diam)
        vol = 1/8 * diam * diam * diam * 4/3 * mathpi
        volList.append(vol)
        count = count + 1
        if diam < 3:
            count_min_3mm = count_min_3mm + 1

    histbase, cumulative, _ = get_cumulative(diamList, 12)

    histbase *= 1000

    opening_max = opening[opening < max(histbase)]

    psd = interp1d(histbase[:-1].tolist(), cumulative.tolist())

    mesh_cumulative = psd(opening_max)

    print("histbase = ", histbase)
    print("max histbase = ", max(histbase))
    print("opening = ", opening_max)
    print("mesh = ", mesh_cumulative)

def enhanceImage(image, lookuptable):
    """Adjust contrast of an image.
    Args:
        imagen (numpy ndarray): numpy ndarray to be adjusted.
        lookuptable (numpy uint8): lookuptable
    Returns:
        numpy ndarray: Contrast adjusted image.
    """
    
    b, g, r = split(image)

    b = LUT(b, lookuptable)
    g = LUT(g, lookuptable)
    r = LUT(r, lookuptable)

    img_rslt = merge([b,g,r])
    return img_rslt

def compress_image(image):
    scale_percent = 50 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = resize(image, dim, interpolation = INTER_AREA)
    encode_param=[int(IMWRITE_JPEG_QUALITY),75]
    result, imgencode = imencode('.jpg', resized, encode_param)
    string_data = np.array(imgencode)
    return string_data



if __name__ == "__main__":
    from smp_ecn import SMPModelo
    import cv2

    image = cv2.imread(r"E:\Biblioteca\CobredelMayo\20210811-250us\2021811-1812.png")
    model_path = r"C:\Users\ivan_\Documents\Python\F80Meter\smp_models\Cobre_del_Mayo\best_multicat_model.pth"
    print("Loading Model %s..." % model_path)
    ecn_model = SMPModelo(model_path)
    print("Model succefully loaded")

    configList = {
        "img_path": "E:/Biblioteca/CerroLindo/20211022_081144.png",
        "rotation": "None",
        "model_path": "C:/Users/ivan_/Documents/Python/F80Meter/F80M_SMP/trained_Models/best_rock_model.pth",
        "lookup_path": "C:/Users/ivan_/OneDrive - electro controles del noroeste/F80METER/1. Proyectos/2. Cobre del Mayo/6. Desarrollo/lookuptable.txt",
        "windowing": [
        256,
        256
        ],
        "origins": [
        500,
        400
        ],
        "offset": 50,
        "NumBoxes": [
        4,
        3
        ],
        "ImgExtract_Point1": [
        0,
        0
        ],
        "ImgExtract_Point2": [
        4096,
        3000
        ],
        "mirror": False,
        "lookup_table_check": False,
        "RectImages": [
        [
            [
            500,
            1100
            ],
            [
            756,
            844
            ]
        ],
        [
            [
            500,
            894
            ],
            [
            756,
            638
            ]
        ],
        [
            [
            500,
            688
            ],
            [
            756,
            432
            ]
        ],
        [
            [
            706,
            1100
            ],
            [
            962,
            844
            ]
        ],
        [
            [
            706,
            894
            ],
            [
            962,
            638
            ]
        ],
        [
            [
            706,
            688
            ],
            [
            962,
            432
            ]
        ],
        [
            [
            912,
            1100
            ],
            [
            1168,
            844
            ]
        ],
        [
            [
            912,
            894
            ],
            [
            1168,
            638
            ]
        ],
        [
            [
            912,
            688
            ],
            [
            1168,
            432
            ]
        ],
        [
            [
            1118,
            1100
            ],
            [
            1374,
            844
            ]
        ],
        [
            [
            1118,
            894
            ],
            [
            1374,
            638
            ]
        ],
        [
            [
            1118,
            688
            ],
            [
            1374,
            432
            ]
        ]
        ],
        "lookup_table": [
        0,
        4,
        8,
        13,
        17,
        22,
        26,
        30,
        35,
        39,
        44,
        48,
        52,
        57,
        61,
        66,
        70,
        75,
        79,
        83,
        88,
        92,
        97,
        101,
        105,
        110,
        114,
        119,
        123,
        128,
        132,
        136,
        141,
        145,
        150,
        154,
        158,
        163,
        167,
        172,
        176,
        180,
        185,
        189,
        194,
        198,
        203,
        207,
        211,
        216,
        220,
        225,
        229,
        233,
        238,
        242,
        247,
        251,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255
        ],
        "SPD_function": "Rosin-Rambler"
    }

    image_p = preprocess_image(image, configList)

    smp_rslt, detect_ratio = smp_detection(image_p, configList, ecn_model)
    print("detect_ratio: %s" % detect_ratio)

    image_dst, segmImag_min, sizeList = segmentation(image_p, smp_rslt)
    real_cumulative, diamList, data_result = cumulative_graph(sizeList, pxlScale)

    Fs, _, _ = data_result

    print("Fs :%s" % Fs)

    image_dst = cv2.resize(image_dst, (1024,750), cv2.INTER_CUBIC)
    cv2.imshow("hello", image_dst)
    cv2.waitKey(0)
    
