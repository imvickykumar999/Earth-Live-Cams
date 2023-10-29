
import cv2
import sys

port = '8080'
ip = '80.32.125.254'

try: url = sys.argv[1]
except: url = f'http://{ip}:{port}/cgi-bin/faststream.jpg'

if url == '0': url = 0
cap = cv2.VideoCapture(url)

while True:
  ret, frame = cap.read()
  
  cv2.imshow('webcam feed' , frame)
  if cv2.waitKey(1) & 0xFF == 27: # use ESC to quit
    break
    
cap.release()
cv2.destroyAllWindows()

'''
>>> python main.py http://158.58.130.148/mjpg/video.mjpg
>>> python main.py http://80.32.125.254:8080/cgi-bin/faststream.jpg
>>> python main.py http://212.147.38.3/mjpg/video.mjpg
'''
