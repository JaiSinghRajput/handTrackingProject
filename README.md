# Hand Tracking and Clicking

This Python script tracks hand movements using a webcam feed and performs mouse clicking actions based on specific gestures. It utilizes the Mediapipe library for hand detection and PyAutoGUI for simulating mouse clicks.

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- PyAutoGUI (`pip install pyautogui`)

## Getting Started

1. Clone the repository or download the Python script (`HandTracking.py`) to your local machine.

2. Install the required dependencies using 
  `pip install -r requirements.txt`
    This will install the necessary Python packages (`opencv-python`, `mediapipe`, and `pyautogui`) for running the script.

3. Run the Python script using the following command:
 ```sh 
 py HandTracking.py
  ```

1. Position your hand in front of the webcam and perform specific gestures to trigger mouse clicking actions.


## How It Works

- The script uses the OpenCV library to capture frames from the webcam feed.

- It utilizes the Mediapipe library for hand detection, extracting hand landmarks from the detected hands.

- Based on the relative positions of specific landmarks (e.g., thumb and index finger), the script determines whether to perform a mouse click action using PyAutoGUI.

## Customization

- You can adjust parameters such as the hand detection confidence thresholds, frame resolution, and smoothing factor for hand movement tracking in the script (`HandTracking.py`) to suit your requirements.

- Experiment with different hand gestures and conditions to fine-tune the gesture recognition and clicking actions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## How to Stop
1. To stop the HandTracking just click on python icon which is show in your task bar then press q for quite