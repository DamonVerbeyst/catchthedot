import cv2import mediapipe as mpfrom utils import get_dot_center, dot_touched, is_left_handprint('OpenCV version:', cv2.__version__)# MediaPipe solution for respectively drawing to the screen and hand landmark detectionmp_drawing = mp.solutions.drawing_utilsmp_hands = mp.solutions.hands# Object to interact with the webcam of your computerwebcam = cv2.VideoCapture(0)# Width and height of the video capture.# This is necessary because drawing a circle using OpenCV uses absolute pixel values, # while the MediaPipe detection returns a relative value between 0 and 1.width, height = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH)), int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))# Arbitrary radius of the dotradius = 30# Parameters for text display on the screentext_font = cv2.FONT_HERSHEY_SIMPLEXtext_org_player_1, text_org_player_2 = (50, 80), (int(width - 700), 80)text_fontScale, text_thickness = 3, 3text_color_player_1, text_color_player_2 = (255, 0, 0), (0, 0, 255)def single_player_game():    score_player_1 = 0    center_coordinates = get_dot_center(width, height, radius)    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1) as hands:        while webcam.isOpened():            ret, frame = webcam.read()            frame = cv2.flip(frame, 1)            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)            results = hands.process(frame)            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)            if results.multi_hand_landmarks:                for num, hand in enumerate(results.multi_hand_landmarks):                    mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)                    tip_x, tip_y = results.multi_hand_landmarks[num].landmark[8].x, results.multi_hand_landmarks[num].landmark[8].y                    tip_x, tip_y = tip_x * width, tip_y * height                    if dot_touched(tip_x, tip_y, center_coordinates[0], center_coordinates[1], radius):                        score_player_1 += 1                        center_coordinates = get_dot_center(width, height, radius)            frame = cv2.circle(frame, center_coordinates, radius=radius, color=(0, 255, 0), thickness=-1)            score_text_player_1 = f'Score p1: {score_player_1}!'            frame = cv2.putText(frame, score_text_player_1, text_org_player_1, text_font, text_fontScale, text_color_player_1, text_thickness, cv2.LINE_AA)            cv2.imshow('Catch The Dot!', frame)            if cv2.waitKey(10) == ord('q'):                break    webcam.release()    cv2.destroyAllWindows()    cv2.waitKey(10)def double_player_game():    score_player_1, score_player_2 = 0, 0    center_coordinates = get_dot_center(width, height, radius)    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=2) as hands:        while webcam.isOpened():            ret, frame = webcam.read()            frame = cv2.flip(frame, 1)            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)            results = hands.process(frame)            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)            if results.multi_hand_landmarks:                for num, hand in enumerate(results.multi_hand_landmarks):                    mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)                    tip_x, tip_y = results.multi_hand_landmarks[num].landmark[8].x, results.multi_hand_landmarks[num].landmark[8].y                    tip_x, tip_y = tip_x * width, tip_y * height                    if dot_touched(tip_x, tip_y, center_coordinates[0], center_coordinates[1], radius):                        if is_left_hand(results, num):                            score_player_1 += 1                        else:                            score_player_2 += 1                        center_coordinates = get_dot_center(width, height, radius)            frame = cv2.circle(frame, center_coordinates, radius=radius, color=(0, 255, 0), thickness=-1)            score_text_player_1 = f'Score p1: {score_player_1}!'            score_text_player_2 = f'Score p2: {score_player_2}!'            frame = cv2.putText(frame, score_text_player_1, text_org_player_1, text_font, text_fontScale, text_color_player_1, text_thickness, cv2.LINE_AA)            frame = cv2.putText(frame, score_text_player_2, text_org_player_2, text_font, text_fontScale, text_color_player_2, text_thickness, cv2.LINE_AA)            cv2.imshow('Catch The Dot!', frame)            if cv2.waitKey(10) == ord('q'):                break    webcam.release()    cv2.destroyAllWindows()    cv2.waitKey(10)