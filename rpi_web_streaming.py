import time
from opencv_camera import VideoCamera
from bottle import route, run, response
@route('/')
def index():
    return """ <html>
             <head>
                <title>Video Streaming Demonstration</title>
             </head>
             <body>
                 <h1>Video Streaming Demonstration</h1>
                 <img src='/video_feed' id='bg' class='img-thumbnail'>
             </body>
             </html>
          """

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@route('/video_feed')
def video_feed():
    response.content_type = 'multipart/x-mixed-replace; boundary=frame'
    return gen(VideoCamera())

run(host='172.30.1.53', post=8000, reloader=True)
