import cv2 as cv #OpenCV Library
import numpy as np  #for handling arrays
#from tqdm.std import tqdm  #for system progressbar
from tqdm.notebook import tqdm #for google colab progressbar
from scipy.spatial import distance  #for cdist 
from time import time # for testing purposes

########################### File Setup #############################
file_name = "pedestrian.mp4"
tot_frame = total_frames(file_name)
cap = cv.VideoCapture(file_name)

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4',fourcc, 25.0,(1282,400))

########################### Bird Eye Transform Setup #############################
corners=[(775,10),(1270,60),(0,350),(1100,700)]  # these are the best looking coordinate I got via hit and trial

tl,tr,bl,br=corners   #top-left, top-right, bottom-left, bottom-right

width1 = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
width2 = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
width_final = max(int(width1), int(width2))

height1 = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
height2 = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
height_final = max(int(height1), int(height2))

static_frame=cv.imread("static_frame_from_video.jpg")
static_frame=cv.resize(static_frame,(1280,720))  # these are the dimensions we are using for the video

persp_matrix, transformed_img = birds_eye_view(corners, width_final, height_final, static_frame)

########################### Making Heading #############################

camera_view_heading = np.zeros((40,640,3),np.uint8)
camera_view_heading_text = "Camera View"
white = (255,255,255)
camera_view_heading = cv.putText(camera_view_heading, camera_view_heading_text, (220, camera_view_heading.shape[0]-13), cv.FONT_HERSHEY_SIMPLEX,0.85, white,2)

bird_eye_heading = np.zeros((40,640,3),np.uint8)
bird_eye_heading_text = "Bird-Eye View"
bird_eye_heading = cv.putText(bird_eye_heading, bird_eye_heading_text, (220, bird_eye_heading.shape[0]-13), cv.FONT_HERSHEY_SIMPLEX,0.85, white,2)

########################### Process The Input #############################
initial_time=time()
for i in tqdm (range (tot_frame), desc="Processing..."): 
    ret,img = cap.read()
    if not ret: break

    birds_display=cv.warpPerspective(img,persp_matrix,(width_final,height_final))
        
    boxes,confidences,centroids=object_detection_YOLO(img, threshold, nms_threshold)
    # box -> x,y,w,h
    # confidence -> confidence of the detected object
    # centroid -> center of the bbox, 2 values list 

    detections=len(boxes)

    # violate=set()  # instead of a set, we can use a dictionary to speed stuff up.
    violate={}

    if detections>1:  # to check if there are at least two people in the frame, otherwise no need to run the algorithm

        transformed_centroids=birds_eye_point(persp_matrix,centroids)
        transformed_centroids=np.array([(int(x),int(y)) for x,y in transformed_centroids])

        # calculates the distance between all the pairs of points
        D=distance.cdist(transformed_centroids,transformed_centroids,metric="euclidean")

        for i in range(D.shape[0]):
            for j in range(i+1, D.shape[1]):
            # check to see if the distance between any two
            # centroid pairs is less than the configured number
            # of pixels
                if D[i, j]<distance_px:
                    # update our violation set with the indexes of
                    # the centroid pairs
                    # violate.add(i)
                    # violate.add(j)
                    violate[i]=1
                    violate[j]=1
                    
        for i in range(detections):
            x, y = boxes[i][0], boxes[i][1]
            w, h = boxes[i][2], boxes[i][3]
            startX, startY, endX, endY = x,y,x+w,y+h
            color = (0, 255, 0)  # green
            # if the index pair exists within the violation set, then
            # update the color
            # if i in violate: color=(0, 0, 255)  # red
            if violate.get(i) is not None: color=(0, 0, 255)
            # draw (1) a bounding box around the person and (2) the
            # centroid coordinates of the person,
            img = cv.rectangle(img, (startX, startY), (endX, endY), color, 2)
            img = cv.circle(img,(centroids[i][0],centroids[i][1]),1,color,10)
            birds_display = cv.circle(birds_display,(transformed_centroids[i][0],transformed_centroids[i][1]),1,color,10)

        # display the rectangle where the bird's magic is happening
        blue = (255,0,0)
        img = cv.line(img,tl,tr,blue,2)
        img = cv.line(img,tl,bl,blue,2)
        img = cv.line(img,bl,br,blue,2)
        img = cv.line(img,tr,br,blue,2)

    # draw the total number of social distancing violations on the output frame
    text = "Social Distancing Violations: {}".format(len(violate))
    img = cv.putText(img, text, (10, img.shape[0]-25), cv.FONT_HERSHEY_SIMPLEX, 0.85, (0, 0, 255), 3)

    output = np.zeros((400,1282,3),img.dtype)

    img_half = cv.resize(img,(640,360)) 
    output[0:40,0:640,0:3] = camera_view_heading
    output[40:400,0:640,0:3] = img_half

    birds_display_half = cv.resize(birds_display,(640,360))
    output[0:40,642:1282,0:3] = bird_eye_heading
    output[40:400,642:1282,0:3] = birds_display_half

    out.write(output)
  
cap.release()
out.release()
print("Processing Completed, Download 'output.mp4' to View Results")
print(f"Time taken to process the input: {time()-initial_time} seconds")