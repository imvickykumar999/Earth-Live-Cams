
import cv2
import numpy as np
import pyautogui
import keyboard

filename = "Screen Record"
screen_size = pyautogui.size()
codec = cv2.VideoWriter_fourcc(*'mp4v')
vid = cv2.VideoWriter(filename + '.mp4', codec, 20, screen_size)

print("Press x key to Stop Recording.")
while True:
    img = pyautogui.screenshot()
    img = np.array(img)
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    vid.write(frame)
    if keyboard.is_pressed('x'):
        break

cv2.destroyAllWindows()
vid.release()
