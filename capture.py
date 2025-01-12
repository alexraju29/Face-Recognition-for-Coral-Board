# ''' module server.py

#     Purpose: implement a basic Flask web server publishing a
#              video stream based on jpg images
# '''


# from flask import Flask, render_template, Response
# from video_camera_for_capture import VideoCameraForCapture

# app = Flask(__name__)


# @app.route('/')
# def capture():
#     ''' function index ...

#     Args: None

#     Returns:
#         rendered index.html template
#     '''
#     return render_template('capture.html')

# @app.route('/video_feed_for_capture')
# def video_feed_for_capture():
#     ''' function video_feed()

#     Function that Flask will be call to retrieve individual frames for the video stream.

#     Args: None

#     returns:
#         jpg frames produced by our video frame generator

#     '''
#     camera = VideoCameraForCapture()
#     return Response(camera.get_frame()),
                    



# @app.route('/capture_image', methods=['POST'])
# def capture_image():
   
#    return render_template(VideoCameraForCapture.capture_image())


# print("Path: ", app.instance_path)
# if __name__ == '__main__':

#     # start local web server
#     app.run(host='0.0.0.0', port='5000', debug=True)



import cv2

# Initialize the webcam (use 0 for the default camera)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not access the camera.")
    exit()

image_count = 0
max_images = 100  # Set the number of images to capture

print(f"Capturing {max_images} images...")

while image_count < max_images:
    # Capture frame-by-frame
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Display the live feed
    cv2.imshow("Live Feed", frame)

    # Save the captured image
    image_filename = f"captured_image_{image_count + 1}.jpg"
    cv2.imwrite(image_filename, frame)
    print(f"Image {image_count + 1} saved as {image_filename}")

    # Increment the image count
    image_count += 1

    # Wait a short time to allow capturing without freezing the feed
    cv2.waitKey(100)  # Delay to avoid high CPU usage (100 ms)

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()

print(f"Captured {max_images} images.")