import cv2


# 가중치 파일 경로
cascade_filename = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
# 모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)


class VideoCamera (object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # image = cv2.resize(image,dsize=None,fx=0.75,fy=0.75)
        img_Gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # cascade 얼굴 탐지 알고리즘
        results = cascade.detectMultiScale(img_Gray, 1.3, 5)
        for (x, y, w, h) in results:
            cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 2)



        ret, jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()
