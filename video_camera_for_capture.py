import os
import select
import threading
import time

# import the necessary packages
from cv2 import VideoCapture, \
                CAP_PROP_FRAME_WIDTH, \
                CAP_PROP_FRAME_HEIGHT, \
                CAP_PROP_FPS, \
                WINDOW_NORMAL, \
                COLOR_BGR2RGB, \
                COLOR_RGB2BGR, \
                namedWindow, \
                cvtColor, \
                imencode, \
                imwrite, \
                waitKey, destroyAllWindows

from numpy import array as np_array

CAMERA_RESOLUTION = (1280, 720)

class VideoCameraForCapture():

    def __init__(self):
        print("Camera images being processed at resolution: {}".format(CAMERA_RESOLUTION))
        destroyAllWindows()
        self.video = VideoCapture(0)
        self.video.set(CAP_PROP_FRAME_WIDTH, CAMERA_RESOLUTION[0])
        self.video.set(CAP_PROP_FRAME_HEIGHT, CAMERA_RESOLUTION[1])
        print("Camera FPS set at {:4.1f}".format(self.video.get(CAP_PROP_FPS)))
        self.frame_as_rgb_array = None # stores the last frame read
        self.success = False
        
        
    def get_frame(self):
        while True:  
            self.success, frame = self.video.read()  
            if not self.success:
                break
            else:
                # Encode frame as JPEG
                _, buffer = imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()
                yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
                self.frame_as_rgb_array = frame
    


    def capture_image(self):
        success, frame = self.video.read() 
        # Ensure training_data directory exists
        os.makedirs('training_data', exist_ok=True)
        # Create a unique filename with timestamp
        timestamp = int(time.time())
        filename = f"training_data/captured_image_{timestamp}.jpg"
        # Save the image
        imwrite(filename, frame)
        print(f"Image captured and saved to {filename}")

        return 'capture.html'