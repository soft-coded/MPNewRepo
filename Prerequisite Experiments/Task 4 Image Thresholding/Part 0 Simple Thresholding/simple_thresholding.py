import cv2 as cv
import numpy as np

def threshold_image_binary(img,threshold):
    x = len(img)
    y = len(img[0]) 
    img_thresholded = np.zeros((x,y),dtype = np.uint8)

    for i in range(0,x):
        for j in range(0,y):
            if img[i][j] > threshold:
                img_thresholded[i][j] = 255
            else:
                img_thresholded[i][j] = 0

    return img_thresholded


img = cv.imread("image.jpg",cv.IMREAD_GRAYSCALE)

threshold = 127

img_thresholded = threshold_image_binary(img,threshold)
cv.imshow("My Edit",img_thresholded)

ret, img_open_source = cv.threshold(img,threshold,255,cv.THRESH_BINARY)
cv.imshow("Open Source",img_open_source)

diff = img_thresholded - img_open_source
cv.imshow("Difference",diff)

cv.waitKey(0)