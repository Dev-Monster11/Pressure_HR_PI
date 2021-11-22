from camera_record import record_video

from multiprocessing import Process
cam_record = Process(target = record_video)
cam_record.start()
cam_record.join()
cam_record.close()