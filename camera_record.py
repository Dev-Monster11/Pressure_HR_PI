import cv2
from video_capture import VideoCaptureAsync
import time
import face_recognition
vid_w = 640
vid_h = 480
capture = VideoCaptureAsync(src=0, width=vid_w, height=vid_h)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')

def record_video():
    capture.start()
    frames = 0
    images = []
    while True:
    # while time.time() <= time_end:
        ret, new_frame = capture.read()

        frames += 1
        frame = new_frame.copy()
        face_location = face_recognition.face_locations(frame)
        if (len(face_location) > 0):
            (top, right, bottom, left) = face_location[0]
            face_image = frame[top:bottom, left:right]
            face_image = face_pixelate(face_image, 5)
            frame[top:bottom, left:right] = face_image
        
        frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)        
        images.append(frame)
        # if frames ==0 or frames%5 == 0:

        # frame = cv2.resize(frame, (vid_w, vid_h))

            # frame = cv2.flip(frame,180)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.stop()
    cv2.destroyAllWindows()
    # fps = frames/duration
    # print(frames)
    # print(fps)
    print(len(images)) 
    out = cv2.VideoWriter('1.mp4', fourcc, 10, (vid_w,vid_h))
    print("creating video")
    for i in range(len(images)):
        out.write(images[i])
    images = []
    print('done')