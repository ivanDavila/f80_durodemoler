#!/usr/bin/env python

'''
Histograma

USAGE:
    Hist.py <image_file>
'''

import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt
import sys

#np.set_printoptions(threshold=sys.maxsize)

import sys
i = 0
imgScale = 1/2
def segmentacionGrande(imageColor, binImage):
    #todos los paraemtros que esten en el argumento son procesados; estos deben ser imagenes
    #la imagen tiene que en escala de grises
    element = np.array([[0,1,0], [1,1,1], [0,1,0]])
    element1 = np.array([[1]])
    element2 = np.array([[1,1,1],[1,1,1],[1,1,1]])
    kernel = np.ones((15,15), np.float32)
    kernel2 = np.ones((3,3), np.uint8)
    imageGray = cv.cvtColor(imageColor, cv.COLOR_RGB2GRAY)
    image_bin = cv.cvtColor(binImage, cv.COLOR_RGB2GRAY)
    image_bin_not = cv.bitwise_not(image_bin)

    height, width = imageGray.shape

    img_eq = cv.equalizeHist(imageGray) #Equalizar image Recortada
    img_bi = cv.bilateralFilter(img_eq, 7, 75, 75, 4)

    blackhat = cv.morphologyEx(img_bi, cv.MORPH_BLACKHAT, kernel) #blackhat-bilat
    rslt = cv.subtract(img_bi, blackhat)
    gauss = cv.GaussianBlur(rslt,(15,15),cv.BORDER_DEFAULT) #se le aplica un Blur Gaussiano

    adapt_thersh = cv.adaptiveThreshold(gauss,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv.THRESH_BINARY,17,2)
    dist_transform = cv.distanceTransform(adapt_thersh,cv.DIST_L2,0)
    ret, th1 = cv.threshold(dist_transform,4.2,255,cv.THRESH_BINARY)
    #Loop though the border pixels and if they are black, floodFill from there

    th1 = np.uint8(th1)

    th1 = th1 - image_bin_not
    # unknown = image_bin - th1
    unknown = cv.subtract(image_bin,th1)
   
    ret, markers = cv.connectedComponents(th1)
    markers = markers+1

    markers[image_bin_not==255] = 1
    markers[unknown==255] = 0

    markers = cv.watershed(imageColor, markers)
    segmn = np.zeros([height,width], dtype=np.uint8)

    for label in np.unique(markers):
        color = list(np.random.choice(range(256), size=3))
        segmn[markers > 1] = 255

    # print("unknown: %s; size: %s" % (unknown.dtype, unknown.shape))
    # resizeimage =  cv.resize(imageColor, (int(width*imgScale),int(height*imgScale)))
    # cv.imshow("markers", resizeimage)
    # cv.waitKey(0)

    return segmn

def segmentacionMin(imageColor, binImage, roiImage):
    #todos los paraemtros que esten en el argumento son procesados; estos deben ser imagenes
    #la imagen tiene que en escala de grises
    element = np.array([[0,1,0], [1,1,1], [0,1,0]])
    element1 = np.array([[1]])
    element2 = np.array([[1,1,1],[1,1,1],[1,1,1]])
    kernel = np.ones((15,15), np.float32)
    kernel2 = np.ones((3,3), np.uint8)
    imageGray = cv.cvtColor(imageColor, cv.COLOR_RGB2GRAY)
    image_bin = cv.cvtColor(binImage, cv.COLOR_RGB2GRAY)

    height, width = imageGray.shape

    img_eq = cv.equalizeHist(imageGray) #Equalizar image Recortada
    img_bi = cv.bilateralFilter(img_eq, 7, 75, 75, 4)

    blackhat = cv.morphologyEx(img_bi, cv.MORPH_BLACKHAT, kernel) #blackhat-bilat
    rslt = cv.subtract(img_bi, blackhat)
    gauss = cv.GaussianBlur(rslt,(15,15),cv.BORDER_DEFAULT) #se le aplica un Blur Gaussiano

    adapt_thersh = cv.adaptiveThreshold(gauss,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv.THRESH_BINARY,17,2)

    tempimag = cv.bitwise_not(cv.bitwise_or(binImage, cv.bitwise_not(roiImage)))
    extract_channel = tempimag[:,:,2]
    # print("adapt_thresh: %s; size: %s" % (adapt_thersh.dtype, adapt_thersh.shape))
    # print("extract_channel: %s; size: %s" % (extract_channel.dtype, extract_channel.shape))
    tempimag = cv.bitwise_and(adapt_thersh, extract_channel)

    dist_transform = cv.distanceTransform(tempimag,cv.DIST_L2,0)
    ret, th1 = cv.threshold(dist_transform,4.2,255,cv.THRESH_BINARY)
    #Loop though the border pixels and if they are black, floodFill from there

    th1 = np.uint8(th1)
    image_tresh_grnlmtria_min = cv.bitwise_and(cv.bitwise_not(binImage), roiImage)
    image_tresh_grnlmtria_min_2d = image_tresh_grnlmtria_min[:,:,2]

    unknown = cv.subtract(image_tresh_grnlmtria_min_2d,th1)
   
    ret, markers = cv.connectedComponents(th1)
    markers = markers+1

    image_bin_not = cv.bitwise_not(image_tresh_grnlmtria_min_2d)

    markers[image_bin_not==255] = 1
    markers[unknown==255] = 0

    rslt[image_tresh_grnlmtria_min_2d == 255] = rslt[image_tresh_grnlmtria_min_2d == 255] + 10
    rslt_color = np.zeros(imageColor.shape)
    rslt_color = cv.cvtColor(rslt, cv.COLOR_GRAY2RGB)

    markers = cv.watershed(image_tresh_grnlmtria_min, markers)
    segmn = np.zeros([height,width], dtype=np.uint8)

    for label in np.unique(markers):
        color = list(np.random.choice(range(256), size=3))
        segmn[markers > 1] = 255
    
    # print("rslt max: %s; size: %s" % (np.amax(rslt), rslt.shape))
    # print("rstl:")
    # resizeimage =  cv.resize(rslt, (int(width*imgScale),int(height*imgScale)))
    # cv.imshow("imageColor", resizeimage)
    # cv.waitKey(0)

    return segmn

def main():
    #todos los paraemtros que esten en el argumento son procesados; estos deben ser imagenes
    if len(sys.argv) > 1:
        for n in range(1, len(sys.argv)):
            fname = sys.argv[n]
            img = cv.imread(fname, 1)

            #Crear constantes para morfologia
            element = np.array([[0,1,0], [1,1,1], [0,1,0]])
            element1 = np.array([[1]])
            element2 = np.array([[1,1,1],[1,1,1],[1,1,1]])
            kernel = np.ones((15,15), np.float32)
            kernel2 = np.ones((3,3), np.uint8)

            height = img.shape[0]
            width = img.shape[1]

            #Se encoge la imagen para que quepa en pantalla
            img_sc = cv.resize(img, (int(width*imgScale),int(height*imgScale)))
            r = cv.selectROI(img_sc)
            imCrop = img[int(r[1]/imgScale):int(r[1]/imgScale+r[3]/imgScale),\
            int(r[0]/imgScale):int(r[0]/imgScale+r[2]/imgScale)]
            
            imCrop_height = imCrop.shape[0]
            imCrop_width = imCrop.shape[1]

            

            gray_imCrop = cv.cvtColor(imCrop, cv.COLOR_BGR2GRAY)
            #Equalizar image Recortada
            img_eq = cv.equalizeHist(gray_imCrop)

            cv.imshow("origi", img_eq)

            img_bi = cv.bilateralFilter(img_eq, 7, 75, 75, 4)
            #img_bi_sc = cv.resize(img_bi, (int(imCrop_height*imgScale),int(imCrop_height*imgScale)))
            #cv.imshow("Image", img_bi)

            #blackhat
            blackhat = cv.morphologyEx(img_bi, cv.MORPH_BLACKHAT, kernel)
            #blackhat = cv.morphologyEx(img_bi, cv.MORPH_GRADIENT, element)
            #cv.imshow("Image2", blackhat)

            #blackhat-bilat
            rslt = cv.subtract(img_bi, blackhat)
            #print(adapt_thersh)
            #rslt = cv.cvtColor(adapt_thersh, 1)
            #print(rslt)

            #se le aplica un Blur Gaussiano
            gauss = cv.GaussianBlur(rslt,(15,15),cv.BORDER_DEFAULT)
            #cv.imshow("Gauss", gauss)

            adapt_thersh = cv.adaptiveThreshold(gauss,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,17,2)

            adapt_thersh2 = cv.erode(adapt_thersh, kernel2, iterations=3)
            
            #RELLENAR HOYOS ADENTRO DE LOS BLOBS
            #copio la imagen thresholiada
            im_floodfill =  adapt_thersh.copy()
            
            #Loop though the border pixels and if they are black, floodFill from there
            print("width = %i" % imCrop_width)
            print("height = %i" % imCrop_height)

            for i in range(imCrop_width):
                if im_floodfill[0,i] == 0:
                    cv.floodFill(im_floodfill, None, (i,0), 255)
                if im_floodfill[0,i] == 0:
                    cv.floodFill(im_floodfill, None, (i,imCrop_height-1), 255)
            
            for i in range(imCrop_height):
                if im_floodfill[i,0] == 0:
                    cv.floodFill(im_floodfill, None, (0,i), 255)
                if im_floodfill[i,0] == 0:
                    cv.floodFill(im_floodfill, None, (imCrop_width-1,i), 255)
            
            
            im_floodfill = cv.bitwise_not(im_floodfill)
            #im_floodfill = im_floodfill + adapt_thersh2

            dist_transform = cv.distanceTransform(adapt_thersh,cv.DIST_L2,0)
            #dist_transform = cv.normalize(dist_transform, 0, 255, cv.NORM_MINMAX)
            ret, th1 = cv.threshold(dist_transform,0.3*dist_transform.max(),255,cv.THRESH_BINARY)
            #ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

            th1 = np.uint8(th1)

            # Marker labelling
            ret, markers = cv.connectedComponents(th1)

            # Add one to all labels so that sure background is not 0, but 1
            #markers = markers+1
            markers = cv.watershed(imCrop, markers)

            for labels in np.unique(markers):
                color = list(np.random.choice(range(256), size=3))
                imCrop[markers == -1] = [0,0,255]
            
            #Se crea una imagen con el tamaño de adapt_thresh2 de putos ceros
            #mask = np.zeros((imwidth+2, imheight+2), np.uint8)

            #print("width = %i"  % imCrop_width)

            #Mascara
            #for i in range(imCrop_width):
            
            # cv.imshow("adapt", imCrop)

            #cv.imshow("makers", markers)

            plt.title('Original Image')
            plt.hist(gray_imCrop.ravel(),256,[0,256])
            plt.figure()

            plt.title('Hist Equalizate')
            plt.hist(img_bi.ravel(),256,[0,256])
            plt.show()
            
        #cv.waitKey(0)
    else:
        print("usage : python dft.py <image1> <image2> ...")

    #im = cv.imread(cv.samples.findFile(fname))

if __name__ == '__main__':
    print(__doc__)
    image_segm = cv.imread("utilities/image_segmented.bmp", 1)
    image_prcess = cv.imread("utilities/preprocessed.bmp", 1)
    image_tresh = cv.imread("utilities/thresh_temp.bmp", 1)

    # image_segm = cv.cvtColor(image_segm, cv.COLOR_RGB2BGR)
    # image_prcess = cv.cvtColor(image_prcess, cv.COLOR_RGB2BGR)

    height, width, _ = image_prcess.shape
    segm = segmentacionGrande(image_segm, image_tresh)
    th2 =  cv.resize(segm, (int(width*imgScale),int(height*imgScale)))
    cv.imshow("hello", th2)
    cv.waitKey()


