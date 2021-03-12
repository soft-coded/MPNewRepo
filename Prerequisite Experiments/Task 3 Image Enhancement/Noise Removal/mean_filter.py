import cv2 as cv
import numpy as np

img = cv.imread("7.tif",cv.IMREAD_GRAYSCALE)

cv.imshow("Original Image",img)

x = len(img)
y = len(img[0])

ans = np.zeros((x,y),dtype = np.uint8 )

for i in range(0,x):
    for j in range(0,y):
        if i == 0 or i == (x-1) or j == 0 or j == (y-1):
            ans[i][j] = img[i][j]
        else:
            array = (img[i-1][j-1], img[i-1][j], img[i-1][j+1], img[i][j-1], img[i][j], img[i][j+1], img[i+1][j-1], img[i+1][j], img[i+1][j+1])
            ans[i][j] = np.floor(np.mean(array))
            
cv.imshow("Mean Filtered Image by Algo",ans)
cv.imwrite("output_algo.tif",ans)

open_source = cv.blur(img,(3,3))
cv.imshow("Median Filtered Image by Open Source",open_source)
cv.imwrite("open_source_algo.tif",open_source)

cv.waitKey(0)