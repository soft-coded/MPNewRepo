import cv2 as cv

file_name = "pedestrians.mp4"

cap = cv.VideoCapture(file_name)

frame_no = 0

while True:
    ret, img = cap.read()

    if(frame_no % 10 == 0):
        cv.imwrite(f"./photos/{frame_no}.png", img)
        print(f"frame {frame_no} done")

    frame_no = frame_no+1

    if not ret:
        break

cap.release()
