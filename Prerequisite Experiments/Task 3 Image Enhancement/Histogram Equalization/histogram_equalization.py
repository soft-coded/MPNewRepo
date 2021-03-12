import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


img = cv.imread('6.tif',cv.IMREAD_GRAYSCALE)
cv.imwrite("greyscale_image.png",img)
cv.imshow("Original Photo",img) 

hist ,bins = np.histogram(img.flatten(),256,[0,256]) 
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max() #only for graph

plt.figure("Histogram and Cumulative Distribution Function")
plt.bar(range(0,256),hist,width=1)
plt.plot(cdf_normalized, color = 'r')
plt.xlim([0,256])
plt.legend(('Histogram','CDF'), loc = 'upper left')

cdf_m = np.ma.masked_equal(cdf,0)   #masking zeros
cdf_m = (cdf_m - cdf_m.min()) / (cdf_m.max() - cdf_m.min()) * 225
cdf = np.ma.filled(cdf_m,0).astype('uint8') #unmasking all zeros

plt.figure("Cumulative Distribution Function Scaled")
plt.bar(range(0,256),cdf,width = 1)
plt.xlim([0,255])

img2 = cdf[img]
cv.imshow("edited",img2)
cv.imwrite("image_edited.png",img2)

plt.figure("Histogram of Edited Image")
plt.hist(img2.flatten(),256,[0,256])

plt.show()