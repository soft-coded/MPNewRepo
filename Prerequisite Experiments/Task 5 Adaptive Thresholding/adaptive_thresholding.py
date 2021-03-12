import cv2 as cv
import numpy as np
'''
def mean_sub_matrix(matrix,i,j,n,c):
    diff = int(np.floor(n/2))

    ret = np.zeros(n**2,np.uint8)
    pos = 0

    for a in range(-1*diff, diff+1):
        for b in range(-1*diff,diff+1):
            ret[pos] = matrix[i+a][j+b]
            pos = pos + 1

    return float(np.mean(ret))-c
'''

'''
def adaptive_threshold_mean(img,n,c):
    temp = np.zeros_like(img)
    x = len(img)
    y = len(img[0])
    diff = int(np.floor(n/2))
    average = cv.blur(img,(n,n),borderType=cv.BORDER_REPLICATE | cv.BORDER_ISOLATED)

    

    for i in range(0,x):
        for j in range(0,y):
            thresh = average[i][j]

            if i <= diff:
                if j <= diff:
                    for a in range(0, diff+1):
                        for b in range(0,diff+1):
                            if(img[i+a][j+b] > thresh):
                                temp[i+a][j+b] = 255
                            else:
                                temp[i+a][j+b] = 0
                elif j >= y - diff:
                    for a in range(0, diff+1):
                        for b in range(-1*diff,0+1):
                            if(img[i+a][j+b] > thresh):
                                temp[i+a][j+b] = 255
                            else:
                                temp[i+a][j+b] = 0
                else:
                    for a in range(0, diff+1):
                        for b in range(-1*diff,diff+1):
                            if(img[i+a][j+b] > thresh):
                                temp[i+a][j+b] = 255
                            else:
                                temp[i+a][j+b] = 0
            elif i >= x - diff:
                if j <= diff:
                   for a in range(-1*diff, 0+1):
                        for b in range(0,diff+1):
                            if(img[i+a][j+b] > thresh):
                                temp[i+a][j+b] = 255
                            else:
                                temp[i+a][j+b] = 0 
                elif j >= y - diff:
                    for a in range(-1*diff, 0+1):
                        for b in range(-1*diff, 0+1):
                            if(img[i+a][j+b] > thresh):
                                temp[i+a][j+b] = 255
                            else:
                                temp[i+a][j+b] = 0
                else:
                    for a in range(-1*diff, 0+1):
                        for b in range(-1*diff, diff+1):
                            if(img[i+a][j+b] > thresh):
                                temp[i+a][j+b] = 255
                            else:
                                temp[i+a][j+b] = 0
            else:
                if j <= diff:
                   for a in range(-1*diff, 0+1):
                        for b in range(0,diff+1):
                            if(img[i+a][j+b] > thresh):
                                temp[i+a][j+b] = 255
                            else:
                                temp[i+a][j+b] = 0 
                elif j >= y - diff:
                    for a in range(-1*diff, 0+1):
                        for b in range(-1*diff, 0+1):
                            if(img[i+a][j+b] > thresh):
                                temp[i+a][j+b] = 255
                            else:
                                temp[i+a][j+b] = 0
                else:
                    for a in range(-1*diff, diff+1):
                        for b in range(-1*diff,diff+1):
                            if(img[i+a][j+b] > thresh):
                                temp[i+a][j+b] = 255
                            else:
                                temp[i+a][j+b] = 0
    
    
    return temp
'''
'''       
def adaptive_threshold_mean(img,n,c):
    temp = np.zeros_like(img)
    x = len(img)
    y = len(img[0])
    diff = int(np.floor(n/2))
    average = cv.blur(img,(n,n),borderType= cv.BORDER_REPLICATE | cv.BORDER_ISOLATED)

    for i in range(diff,x-diff):
        for j in range(diff,y-diff):
            thresh = mean_sub_matrix(img,i,j,n,c)
            for a in range(-1*diff, diff+1):
                    for b in range(-1*diff,diff+1):
                        if(img[i+a][j+b] > thresh):
                            temp[i+a][j+b] = 255
                        else:
                            temp[i+a][j+b] = 0
    return temp
'''
'''
def adaptive_threshold_mean(img,n,c):
    
    x = len(img)
    y = len(img[0])

    average = np.zeros_like(img)
    average = cv.blur(img,(n,n),average,borderType= cv.BORDER_REPLICATE|cv.BORDER_ISOLATED)
    temp = np.zeros_like(img)
    diff = int(np.floor(n/2))

    for i in range(diff,x-diff):
        for j in range(diff,y-diff):
            thresh = average[i][j] - c
            for a in range(-1*diff, diff+1):
                    for b in range(-1*diff,diff+1):
                        if(img[i+a][j+b] > thresh):
                            temp[i+a][j+b] = 255
                        else:
                            temp[i+a][j+b] = 0
    return temp
'''
    


img = cv.imread("image.bmp",cv.IMREAD_GRAYSCALE)

img_open_source = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,17)
cv.imshow("Open Source ",img_open_source)




#img_my = adaptive_threshold_mean(img,3,3)
#cv.imshow("My",img_my)
#cv.imshow("original",img)

#diff = img_my - img
#cv.imshow("Diff",diff)

cv.waitKey(0)

'''
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],dtype= np.uint8)




b= adaptive_threshold_mean(a,3,0)

c= cv.adaptiveThreshold(a,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,3,0)




print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
'''
