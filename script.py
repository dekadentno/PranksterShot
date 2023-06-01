import cv2
import os
import time
import sys
from datetime import datetime
from pynput import keyboard, mouse

PHOTO_LIMIT = 5
WAIT_TIME = 5

photo_counter = 0

mouse_listener = mouse.Listener()
keyboard_listener = keyboard.Listener()

# dir for storing photos
run_timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
photo_directory = f'snaps/run_{run_timestamp}'
os.makedirs(photo_directory, exist_ok=True)

# call whenever a mouse move is detected
def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    global photo_counter
    if pressed:
        photo_counter += 1
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        cv2.imwrite(f'{photo_directory}/webcam_pic{photo_counter}_{timestamp}.jpeg', frame)
        cap.release()
        if photo_counter >= PHOTO_LIMIT:
            os.system('mate-screensaver-command -l')
            mouse_listener.stop()
            keyboard_listener.stop()
            sys.exit(0)

# call whenever a keyboard key is pressed
def on_press(key):
    global photo_counter
    photo_counter += 1
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    cv2.imwrite(f'{photo_directory}/webcam_pic{photo_counter}_{timestamp}.jpeg', frame)
    cap.release()
    if photo_counter >= PHOTO_LIMIT:
        os.system('mate-screensaver-command -l')
        mouse_listener.stop()
        keyboard_listener.stop()
        sys.exit(0)

# when the script runs, wait for a defined time before continuing
time.sleep(WAIT_TIME)

# Starting the mouse listener
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)
mouse_listener.start()

# Starting the keyboard listener
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

try:
    keyboard_listener.join()
    mouse_listener.join()
except KeyboardInterrupt:
    pass
