import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def otsu_threshold (img):
    hist = cv.calcHist([img],[0],None,[256],[0,256])  
    hist_norm = np.divide(hist.ravel(),hist.sum()) 
    q = hist_norm.cumsum()

    bins = np.arange(256)

    fn_min = np.inf
    threshold = -1

    for i in range(1,256):
        p1,p2 = np.hsplit(hist_norm,[i])

        q1 , q2 = q[i] , q[255]-q[i]
    
        if q1 < 1.e-6 or q2 < 1.e-6:
            continue

        b1 , b2 = np.hsplit(bins,[i])

        m1 = np.sum(p1 * b1)/q1   
        m2 = np.sum(p2 * b2)/q2

        v1 = np.sum( ((b1 - m1)**2) * p1)/q1
        v2 = np.sum( ((b2 - m2)**2) * p2)/q2

        fn = v1*q1 + v2*q2

        if fn < fn_min:
            fn_min = fn
            threshold = i

    return threshold



img = cv.imread("input.jpg",0)  

threshold = otsu_threshold(img)

a, img_my = cv.threshold(img,threshold,255,cv.THRESH_BINARY)
cv.imshow("My",img_my)

ret , img_os = cv.threshold(img,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow("OS",img_os)

#cv.imwrite("output.jpg",img_my)

cv.waitKey(0)

