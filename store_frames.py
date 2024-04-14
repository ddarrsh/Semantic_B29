import cv2
import requests


def store(path):
    capture = cv2.VideoCapture(path)
    frameNr = 0
    while True:
        success, frame = capture.read()
        if success:
            cv2.imwrite(f'extracted_frames/frame_{frameNr}.jpg', frame)
        else:
            break
        frameNr = frameNr + 1
    capture.release()














def check():
    url = "http://www.google.com"
    timeout = 5  # Timeout in seconds
    try:
        # Try to send a GET request to google.com
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Internet is connected!")
    except requests.RequestException as e:
        # If an exception occurs, it means there's no internet connectivity
        print("NLP MODEL CANNOT BE LOADED")

