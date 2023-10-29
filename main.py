
import cv2

ip = '80.32.125.254'
port = '8080'

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(f'http://{ip}:{port}/cgi-bin/faststream.jpg')

while True:
  ret, frame = cap.read()
  
  cv2.imshow('webcam feed' , frame)
  if cv2.waitKey(1) and 0xFF == ord('q'):
    break
    
cap.release()
cv2.destroyAllWindows()
