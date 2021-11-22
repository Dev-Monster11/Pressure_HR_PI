import threading
import time
import cv2
import face_recognition

from blurring import face_simple, face_pixelate
# Define video capture class
class VideoCaptureAsync:
    def __init__(self, src=0, width=640, height=480, driver=None):
        self.src = src
        if driver is None:
            self.cap = cv2.VideoCapture(self.src)
        else:
            self.cap = cv2.VideoCapture(self.src, driver)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.grabbed, self.frame = self.cap.read()
        self.started = False
        self.read_lock = threading.Lock()
        self.thread = None

    def get(self, var1):
        return self.cap.get(var1)

    def set(self, var1, var2):
        self.cap.set(var1, var2)

    def start(self):
        if self.started:
            print('[!] Asynchroneous video capturing has already been started.')
            return None
        self.started = True
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):
        while self.started:

            grabbed, frame = self.cap.read()
            with self.read_lock:

                self.grabbed = grabbed
                face_location = face_recognition.face_locations(frame)
                if (len(face_location) > 0):
                    (top, right, bottom, left) = face_location[0]
                    face_image = frame[top:bottom, left:right]
                    face_image = face_pixelate(face_image, 5)
                    frame[top:bottom, left:right] = face_image
                
                self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    def read(self):
        with self.read_lock:
            frame = self.frame.copy()
            grabbed = self.grabbed
        return grabbed, frame

    def stop(self):
        self.started = False
        self.thread.join()

    def __exit__(self, exec_type, exc_value, traceback):
        self.cap.release()