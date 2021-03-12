import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def compute_histogram(image_matrix):
    x = len(img)
    y = len(img[0])

    count = np.zeros(265)

    for j in range(0,x):
        for k in range(0,y):
            count[img[j,k]] = count[img[j,k]] + 1

    return count


img = cv.imread('image.png',cv.IMREAD_GRAYSCALE)

cv.imshow("Image",img)
k = cv.waitKey(100)
cv.imwrite('greyscale.png',img)

plt.figure(1)
histogram = compute_histogram(img)
plt.stem(histogram, markerfmt = ' ')
plt.xlabel("Grayscale Values")
plt.ylabel("No. Of Occurence")
plt.title("Using compute_histogram()")


plt.figure(2)
plt.hist(img.ravel(),256,[0,256])
plt.xlabel("Grayscale Values")
plt.ylabel("No. Of Occurence")
plt.title("Using In-Built Commands")
plt.show()
