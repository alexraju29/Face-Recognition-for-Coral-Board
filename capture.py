''' module server.py

    Purpose: implement a basic Flask web server publishing a
             video stream based on jpg images
'''


from flask import Flask, render_template, Response
from video_camera import VideoCamera, VideoCameraForCapture

app = Flask(__name__)


@app.route('/')
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
    camera = VideoCameraForCapture()
    return Response(camera.get_frame()),
                    



@app.route('/capture_image', methods=['POST'])
def capture_image():
   
   return render_template(VideoCameraForCapture.capture_image())


print("Path: ", app.instance_path)
if __name__ == '__main__':

    # start local web server
    app.run(host='0.0.0.0', port='5000', debug=True)

