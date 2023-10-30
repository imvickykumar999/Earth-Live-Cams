
import cv2
import sys
import time

port = '8080'
ip = '80.32.125.254'

try: url = sys.argv[1]
except: url = f'http://{ip}:{port}/cgi-bin/faststream.jpg'

if url == '0': url = 0
cap = cv2.VideoCapture(url)

file = time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime())
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter(f'Recorded/{file}_main.avi', fourcc, 20.0, (640, 480)) 

while True:
  ret, frame = cap.read()
  out.write(frame)  

  cv2.imshow('webcam feed' , frame)
  if cv2.waitKey(1) & 0xFF == 27: # use ESC to quit
    break
    
cap.release()
cv2.destroyAllWindows()

'''
>>> python main.py http://80.32.125.254:8080/cgi-bin/faststream.jpg
>>> python main.py http://212.147.38.3/mjpg/video.mjpg
>>> python main.py http://212.26.235.210/mjpg/video.mjpg
>>> python main.py http://imvickykumar999:imvickykumar999@192.168.0.101:8080/video
>>> python main.py 0
'''
