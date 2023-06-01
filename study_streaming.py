import time
from study_detect import VideoCamera
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
        #Content-Type에서 '-'빠지면 스트리밍 안된다.
@route('/video_feed')
def video_feed():
    response.content_type = 'multipart/x-mixed-replace; boundary=frame'
    #'multipart/x-mixed-replace'에서 '-'빠지면 스트리밍 안된다.
    return gen(VideoCamera())

run(host='172.20.10.3', post=8000, reloader=True)
