''' module server.py

    Purpose: implement a basic Flask web server publishing a
             video stream based on jpg images
'''

import time
import argparse
from flask import Flask, render_template, Response
from video_camera import VideoCamera, VideoCameraForCapture

app = Flask(__name__)

@app.route('/')
def index():
    ''' function index ...

    Args: None

    Returns:
        rendered index.html template
    '''
    return render_template('index.html')

def gen(camera):
    ''' function gen

    A Generator producing the jpg images that will be served as the frames for the video stream

    Args:
        camera (VideoCamera): Instance of a VideoCamera that will provide the jpg images

    Yields:
        individual video frames that are jpg encoded
    '''
    while True:
        frame = camera.get_frame()
        if frame is not None:
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
        else:
            # Sleep 10ms to avoid a really tight loop if there's no frame ready
            time.sleep(.01)

@app.route('/video_feed')
def video_feed():
    ''' function video_feed()

    Function that Flask will be call to retrieve individual frames for the video stream.

    Args: None

    returns:
        jpg frames produced by our video frame generator
    '''
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/capture', methods=['POST'])
def capture():
    ''' function index ...

    Args: None

    Returns:
        rendered index.html template
    '''
    return render_template('capture.html')

@app.route('/video_feed_for_capture')
def video_feed_for_capture():
    ''' function video_feed()

    Function that Flask will be call to retrieve individual frames for the video stream.

    Args: None

    returns:
        jpg frames produced by our video frame generator
    '''
    return Response(VideoCameraForCapture.get_frame()),
                    



@app.route('/capture_image', methods=['POST'])
def capture_image():
   
   return render_template(VideoCameraForCapture.capture_image())




print("Path: ", app.instance_path)
if __name__ == '__main__':

    # start local web server
    app.run(host='0.0.0.0', port='5000', debug=True)
