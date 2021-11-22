import cv2
from video_capture import VideoCaptureAsync
import time

vid_w = 640
vid_h = 480
capture = VideoCaptureAsync(src=0, width=vid_w, height=vid_h)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

def record_video():
    capture.start()
    frames = 0
    images = []
    while True:
    # while time.time() <= time_end:
        ret, new_frame = capture.read()
        frames += 1
        images.append(new_frame)
        if frames ==0 or frames%5 == 0:

            frame = cv2.resize(new_frame,(640,480))
            frame = cv2.flip(frame,180)
            cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.stop()
    cv2.destroyAllWindows()
    # fps = frames/duration
    # print(frames)
    # print(fps)
    print(len(images)) 
    out = cv2.VideoWriter('video.avi', fourcc, 10, (vid_w,vid_h))
    print("creating video")
    for i in range(len(images)):
        out.write(images[i])
    images = []