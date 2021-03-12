import cv2 as cv
import numpy as np
import scipy.stats as st

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
            mode = st.mode(array)
            ans[i][j] = mode[0]
            
cv.imshow("Median Filtered Image by Algo",ans)
cv.imwrite("output_algo.tif",ans)

cv.waitKey(0)