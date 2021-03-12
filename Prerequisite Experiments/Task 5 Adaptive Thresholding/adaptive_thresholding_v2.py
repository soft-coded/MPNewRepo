import cv2 as cv
import numpy as np

def adaptive_threshold(img, blocksize,diff):
    avg = cv.blur(img,(blocksize,blocksize),borderType = cv.BORDER_REPLICATE | cv.BORDER_ISOLATED) - np.ones_like(img)*diff
    output = np.zeros_like(img)
    x = len(img)
    y = len(img[0])

    for i in range(0,x):
        for j in range(0,y):
            if(img[i][j] < avg[i][j]):
                output[i][j] = 0
            else:
                output[i][j] = 255
    return output

img = cv.imread("input.bmp",cv.IMREAD_GRAYSCALE)

blocksize = 11
diff = 19

output = adaptive_threshold(img,blocksize,diff)

opensource = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,blocksize,diff)

cv.imshow("opensource", opensource)
cv.imshow("output",output)
cv.waitKey(0)