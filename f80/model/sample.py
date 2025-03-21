import cv2

image = cv2.imread(r"E:\Biblioteca\cerrolindo\CerroLindo_20211116\20211022_081050.png")
image_dst = cv2.resize(image, (1024,750), cv2.INTER_CUBIC)
cv2.imshow("hello", image_dst)
cv2.waitKey(0)