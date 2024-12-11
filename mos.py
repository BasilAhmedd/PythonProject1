import cv2
import numpy as np

video = cv2.VideoCapture("D:\outputterminated.mp4")

while True:
    ret,frame = video.read()
    if not ret:
        break

    yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

    yuv_frame[:,:,0] = cv2.equalizeHist(yuv_frame[:,:,0])

    corrected_frame = cv2.cvtColor(yuv_frame, cv2.COLOR_YUV2BGR)
    cv2.imshow("Video", corrected_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break