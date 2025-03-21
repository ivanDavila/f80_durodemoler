import cv2
from os import listdir
from os.path import abspath, dirname, isfile, join

def simcamera(image_dir):
    for fle , name in listFiles(image_dir):
        yield cv2.imread(fle,1), name

def listFiles(directorypath): #enlista todos los archivos en un folder
    for fileName in listdir(directorypath):
        if isfile(join(directorypath, fileName)):
            xfile = join(directorypath, fileName)
            #xfile = 'hello'
            yield xfile, fileName

inputdir = 'D:\Biblioteca\cerrolindo\OneDrive_2022-02-15'
outputdir = 'D:\Biblioteca\cerrolindo\imagenes_rec'

def main():
    for image, name in simcamera(inputdir):
        image_rec = image[750:2250, 1012:3036]
        print(name)
        output_im_path = outputdir + '/' + name
        cv2.imwrite(output_im_path, image_rec)

if __name__ == "__main__":
    main()





