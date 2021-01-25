import cv2 as cv #OpenCV Library
import numpy as np  #for handling arrays

# Give the configuration and weight files for the model and load the network.
net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')  # Reads Network from .cfg and .weights
net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)   # this specifies what type of hardware to use (GPU or CPU)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)     # sets preferable hardware

threshold = 0.75
nms_threshold = 0.012
distance_px=120   # arbitrary value for now but looked best

def object_detection_YOLO(img,threshold,nms_threshold):
    # determine the output layers
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    # construct a blob from the image
    # blob is just a preprocessed image
    blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)      #blob = boxes
    # blobs goes as the input to YOLO
    # inputting blob to the Neural Network
    net.setInput(blob)
    # t0 = time.time()
    outputs = net.forward(ln)   # finds output
    # t = time.time()
    # print('time=', t-t0)

    boxes = []
    confidences = []
    centroids = []
    results = []

    h, w = img.shape[:2]
    for output in outputs:  # Outputs have all the detection and their probability for every class
        for detection in output:    # detection is the the list of all probabilities with box dimension in start
            scores = detection[5:]  # everything in array after 5th element
            classID = np.argmax(scores)     # picks the maximum probability
            confidence = scores[classID] 

            if (confidence > threshold) and (classID == 0):
                #first 4 elements are box characteristics normalized to range(0,1)
                #first two element are middle co-ordinate
                # next two are width and height of blob           
                box = detection[:4] * np.array([w, h, w, h])    
                (centerX, centerY, width, height) = box.astype("int")   # typecasting to int, as array indexes are int
                x = int(centerX - (width / 2))      # finding upper corner
                y = int(centerY - (height / 2))
                box = [x, y, int(width), int(height)]   # changing origin to top left and typecasted to int
                boxes.append(box)                       # added the box to boxes
                confidences.append(float(confidence))   # added confidence to confidences
                centroids.append((centerX,centerY))

    indices = cv.dnn.NMSBoxes(boxes, confidences,score_threshold=threshold,nms_threshold=nms_threshold)
    # score_threshold -> threshold for confidence
    # nms_threshold -> threshold for how close to blobs are, if two blobs are too close, one of them is discarded
    # closeness is determined by IoU (intersection over Union)
    # discarding is based on confidence, higher confidence is retained

    boxes_final=[]; confidences_final=[]; centroids_final=[]
    if len(indices):
        for i in indices.flatten():
            # extract the bounding box coordinates
            x, y = (boxes[i][0], boxes[i][1])
            w, h = (boxes[i][2], boxes[i][3])
            boxes_final.append((x,y,w,h))
            confidences_final.append(confidences[i])
            centroids_final.append(centroids[i])

    return boxes_final,confidences_final,centroids_final