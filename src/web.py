
import http.server
import socketserver
import time
import cv2
import threading 
import sys

PORT = 8080
ip = '80.32.125.254'

try: url = sys.argv[1]
except: url = f'http://{ip}:{PORT}/cgi-bin/faststream.jpg'

if url == '0': url = 0
cap = cv2.VideoCapture(url)

file = time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime())
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter(f'Recorded/{file}_web.avi', fourcc, 20.0, (640, 480)) 

pageData = "<!DOCTYPE>" + \
            "<html>" + \
            "  <head>" + \
            "    <title>HttpListener Example</title>" + \
            "  </head>" + \
            "  <body>" + \
            "  <br><br><br>" + \
            "  <center>" + \
            "<img id=\"image\"/>"+ \
            " <script type=\"text/javascript\">var image = document.getElementById('image');function refresh() {image.src = \"/image?\" + new Date().getTime();image.onload= function(){setTimeout(refresh, 30);}}refresh();</script>   "+ \
            "  </center>" + \
            "  </body>" + \
            "</html>"

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(pageData, "utf8"))
        elif self.path.startswith('/image'):
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()

            self.wfile.write(jpg)
        else:
            self.send_response(404)
         
ret, frame = cap.read()
_, jpg = cv2.imencode(".jpg", frame)
  
class FrameThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.isRunning = True

    def run(self):
        global jpg, cap

        while self.isRunning:
            ret, frame = cap.read()
            out.write(frame)  

            _, jpg = cv2.imencode(".jpg", frame)
            time.sleep(0.03)

        print("Quit thread")

frame_thread = FrameThread()
frame_thread.start()

with socketserver.TCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    print("Serving at http://127.0.0.1:8080/")
    try:
        httpd.serve_forever()
    except:
        pass

print('Server is stopped')
frame_thread.isRunning = False
frame_thread.join()
cap.release()

'''
>>> python web.py http://158.58.130.148/mjpg/video.mjpg
>>> python web.py http://80.32.125.254:8080/cgi-bin/faststream.jpg
>>> python web.py http://212.147.38.3/mjpg/video.mjpg
>>> python web.py http://212.26.235.210/mjpg/video.mjpg
>>> python web.py http://imvickykumar999:imvickykumar999@192.168.0.101:8080/video
>>> python web.py 0
'''
