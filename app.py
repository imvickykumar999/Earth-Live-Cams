
# # from HostTor import VicksTor
# import VicksTor
# VicksTor.run_server('flask')

import cv2, sys, time
from flask import (
    Flask, 
    render_template, 
    Response
)
app = Flask(__name__)

port = '8080'
ip = '80.32.125.254'

try: url = sys.argv[1]
except: url = f'http://{ip}:{port}/cgi-bin/faststream.jpg'

if url == '0': url = 0
cap = cv2.VideoCapture(url)

file = time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime())
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter(f'src/Recorded/{file} app.mp4', fourcc, 20.0, (640, 480)) 

def generate_frames():
    while True:

        success, frame = cap.read()
        out.write(frame)  

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield(b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__=="__main__":
    app.run(
        host='0.0.0.0',
        debug=False
    )
    out.release()

'''
>>> python app.py http://80.32.125.254:8080/cgi-bin/faststream.jpg
>>> python app.py http://212.147.38.3/mjpg/video.mjpg
>>> python app.py http://212.26.235.210/mjpg/video.mjpg
>>> python app.py http://imvickykumar999:imvickykumar999@192.168.0.101:8080/video
>>> python app.py 0
'''
