#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:20:28 2024

@author: damon
"""

# ___Importing libraries___
import mediapipe as mp
import cv2
import random
from math import sqrt


# ___Auxiliary Functions___

# This function randomly generates a center coordinate for a new dot.
# The function makes sure that the circle can always be fully displayed on the screen.
def get_dot_center(width, height, radius=30):
    c_x = random.randrange(radius, width-radius)
    c_y = random.randrange(radius, height-radius)
    return (c_x, c_y)

# This function returns true when the euclidean distance between the tip of the index finger 
# and the center of the dot is smaller than the radius of the dot.
def dot_touched(tip_x, tip_y, c_x, c_y, radius):
    distance = sqrt((c_x-tip_x)*(c_x-tip_x)+(c_y-tip_y)*(c_y-tip_y))
    return distance < radius


# ___Main script___

# MediaPipe solution for respectively drawing to the screen and hand landmark detection
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


# arbitrary radius of the dot
radius = 30

# parameters for text display on the screen
text_font = cv2.FONT_HERSHEY_SIMPLEX 
text_org = (50, 80) 
text_fontScale = 3
text_color = (255, 0, 0)
text_thickness = 3

# score of the player
score = 0

# Object to interact with the webcam of your computer
webcam = cv2.VideoCapture(0)

# Width and height of the video capture.
# This is necessary because drawing a circle using OpenCV uses absolute pixel values, 
# while the MediaPipe detection returns a relative value between 0 and 1.
width, height = webcam.get(cv2.CAP_PROP_FRAME_WIDTH), webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)



# the center coordinates of the initial dot on the screen
center_coordinates = get_dot_center(width, height, radius)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1) as hands:
    
    while webcam.isOpened():

        # Read in frames while the webcam is open
        ret, frame = webcam.read()

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)
        
        # MediaPipe operates on the RGB color-scheme
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Apply the MediaPipe hand detection model on the frame
        results = hands.process(frame)
        
        # Convert back to the original BGR color-scheme
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
               
        # Drawing connected landmarks (joints)
        if results.multi_hand_landmarks:
            # Iterate over hands (only 1 in this case)
            for num, hand in enumerate(results.multi_hand_landmarks):
                # Draw the landmarks
                mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
                
                # Extract the position of landmark 8: the tip of the index finger
                tip_x, tip_y = results.multi_hand_landmarks[0].landmark[8].x, results.multi_hand_landmarks[0].landmark[8].y
                tip_x, tip_y = tip_x * width, tip_y * height
                
                # Check if the player managed to catch the dot
                if dot_touched(tip_x, tip_y, center_coordinates[0], center_coordinates[1], radius):
                    score += 1
                    # Generate new center coordinates for the dot
                    center_coordinates = get_dot_center(width, height, radius)
                
        # Draw dot to the screen
        # Thickness is set to a negative value in order to fill the circle
        frame = cv2.circle(frame, center_coordinates, radius=radius, color=(255, 0, 0), thickness=-1)
        
        
        score_text = 'Score: ' + str(score) + '!'
        frame = cv2.putText(frame, score_text, text_org, text_font, text_fontScale, text_color, text_thickness, cv2.LINE_AA) 

        # Display the frame on the screen
        cv2.imshow('Catch The Dot!', frame)

        # Interrupt the webcam stream when users press the 'q' key (quit)          
        key = cv2.waitKey(10)
        if key == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()

cv2.waitKey(10)