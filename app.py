
# from HostTor import VicksTor
import VicksTor
VicksTor.run_server('flask')

import cv2
from flask import (
    Flask, 
    render_template, 
    Response
)

app = Flask(__name__)
# port = '8080'
# ip = '192.168.0.101'

# username = 'imvickykumar999'
# password = 'imvickykumar999'

# camera = cv2.VideoCapture(0) # laptop webcam
# camera = cv2.VideoCapture(f'http://{ip}:{port}/video') # no authentication
# camera = cv2.VideoCapture(f'http://{username}:{password}@{ip}:{port}/video')

ip = '80.32.125.254'
port = '8080'

def generate_frames():
    while True:
        camera = cv2.VideoCapture(f'http://{ip}:{port}/cgi-bin/faststream.jpg')

        success, frame = camera.read()
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
