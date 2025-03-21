import datetime

from cv2 import imwrite
from os import makedirs, walk
from os.path import exists, getsize
from pathlib import Path
from threading import Thread

def save_image_thread(image_folder, image):
    save_im_thread = Thread(
        target=save_image, 
        args=(image_folder, image))
    save_im_thread.daemon = False
    save_im_thread.start()


def save_image(image_folder, image):
    currentDT = datetime.datetime.now()
    image_folder = Path(image_folder)
    im_fldr_date = image_folder / Path("%04d%02d%02d" % (
        currentDT.year,
        currentDT.month,
        currentDT.day
        ))

    if not exists(im_fldr_date):
        makedirs(im_fldr_date)
        print("Directory " , im_fldr_date ,  " Created ")
    else:    
        print("Directory " , im_fldr_date ,  " already exists")  
    
    image_path = im_fldr_date / Path("%04d%02d%02d-%02d%02d%02d.png" % (
        currentDT.year,
        currentDT.month,
        currentDT.day,
        currentDT.hour,
        currentDT.minute,
        currentDT.second
        ))
    
    imwrite(str(image_path), image)

def file_size(folder_path):
    fsize = 0
    for (dir, _, filenames) in walk(folder_path):
        for fle in filenames:
            f = str(dir) + "\\" + fle
            fsize += getsize(f)   
    return fsize