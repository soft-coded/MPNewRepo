import cv2 as cv

img = cv.imread("image.png",cv.IMREAD_UNCHANGED)
cv.imshow("Image",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",gray)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("grayscale.png",gray)