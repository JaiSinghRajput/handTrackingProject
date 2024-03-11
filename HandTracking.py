import cv2
import mediapipe as mp
import pyautogui
import threading

def hand_tracking():
    hand_detector = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    index_clicked = False
    prev_index_x, prev_index_y = 0, 0
    smoothed_index_x, smoothed_index_y = 0, 0
    alpha = 0.5  # Smoothing factor

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue
        
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        small_frame = cv2.resize(frame_rgb, (0, 0), fx=0.6, fy=0.6)
        results = hand_detector.process(small_frame)
        
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            thumb = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
            index_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_x = int(thumb.x * screen_width)
            thumb_y = int(thumb.y * screen_height)
            index_x = int(index_finger.x * screen_width)
            index_y = int(index_finger.y * screen_height)
            smoothed_index_x = alpha * smoothed_index_x + (1 - alpha) * index_x
            smoothed_index_y = alpha * smoothed_index_y + (1 - alpha) * index_y
            pyautogui.moveTo(int(smoothed_index_x), int(smoothed_index_y), duration=0)
            if abs(index_y - thumb_y) < 25:
                if not index_clicked:
                    pyautogui.click()
                    index_clicked = True
            else:
                index_clicked = False
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    print("Hand tracking started...")
    # Start hand tracking in a separate thread
    tracking_thread = threading.Thread(target=hand_tracking)
    tracking_thread.start()

if __name__ == "__main__":
    main()
