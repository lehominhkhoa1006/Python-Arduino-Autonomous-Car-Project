#VEHICLE AUTOMATIC CONTROL SYSTEM
#VACS330333E_23_2_01FIE-HCMUTE
#GROUP_4
import cv2
import numpy as np
import math
import serial
import time

threshold1 = 90  #Reduce Canny threshold to enhance edge detection
threshold2 = 150  #Reduce Canny threshold to enhance edge detection
theta = 0
r_width = 640  #Reduce frame size
r_height = 480  #Reduce frame size
minLineLength = 100
maxLineGap = 10
k_width = 5
k_height = 5
max_slider = 10

def region_of_interest(edges):
        height = frame.shape[0]
        width = frame.shape[1]
        mask = np.zeros_like(edges)
        triangle = np.array([[
        (0,height-5), #Left_Bottom
        (width*(0.20), height*(0.4)),#Left_Top
        (width*(0.67), height*(0.4)),#Right_Top
        (width, height-5 ),]], np.int32) #Right_Bottom
        cv2.fillPoly(mask, triangle, 255)
        masked_image = cv2.bitwise_and(edges, mask)
        return masked_image


frame_count = 0  #Frame count variable
send_count = 0  #Counter variable sends data

cap = cv2.VideoCapture(0)
ser = serial.Serial('COM7', 115200)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    if frame_count % 3 != 0:  #Only process frames every 3 times
        continue
    
    # Resize width=400 height=225
    frame = cv2.resize(frame, (r_width, r_height))
    
    # Convert the image to gray-scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (k_width, k_height), 0)
        
    # Find the edges in the ROI using Canny detector
    edged = cv2.Canny(blurred, threshold1, threshold2, apertureSize = 3)

    #Limmited region
    crop_canny=region_of_interest(edged)
    
    # Detect points that form a line
    lines = cv2.HoughLinesP(crop_canny, 1, np.pi/180, max_slider, minLineLength, maxLineGap)
    
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi  #Calculate the angle of the line
                if abs(angle) < 45:  #Remove lines that are close to horizontal
                   continue
                cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 3)  #Redraw the line on the original frame
                theta += math.atan2((y2 - y1), (x2 - x1))
    
    threshold = 5
    if theta > threshold:
        print("Go left")
        send_count += 1
        if send_count % 3 == 0:  #Send data every 3 times
            ser.write(b'L')  #Send left signal to Arduino
    elif theta < -threshold:
        print("Go right")
        send_count += 1
        if send_count % 3 == 0:  #Send data every 3 times
            ser.write(b'R')  #Send signal right to Arduino
    else:
        print("Go straight")
        send_count += 1
        if send_count % 3 == 0:  #Send data every 3 times
            ser.write(b'S')  #Send stop signal to Arduino
    
    theta = 0
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Edged", edged)
    cv2.imshow('cropped pic',crop_canny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
