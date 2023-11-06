
import cv2, time, sys

port = '8080'
ip = '192.168.0.103'
username = 'imvickykumar999'
password = 'imvickykumar999'

try: url = sys.argv[1]
except: url = f'http://{username}:{password}@{ip}:{port}/video'

if url == '0': url = 0
cap = cv2.VideoCapture(url)

file = time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime())
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter(f'{file} main.mp4', fourcc, 20.0, (640, 480)) 

while True:
	ret, frame = cap.read()
	face_detect = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') 
	face_data = face_detect.detectMultiScale(frame, 1.3, 5) 

	for (x, y, w, h) in face_data: 
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
		roi = frame[y:y+h, x:x+w] 
		roi = cv2.GaussianBlur(roi, (23, 23), 30) 
		frame[y:y+roi.shape[0], x:x+roi.shape[1]] = roi

	out.write(frame)  
	cv2.imshow('Main - ESC to Quit' , frame)
	if cv2.waitKey(1) & 0xFF == 27:
		break
    
cap.release()
out.release()
cv2.destroyAllWindows()

'''
>>> python face_blur.py 0
'''
