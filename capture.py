import cv2

# Define the directory to save images
save_dir = 'training_data/data'
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
    image_filename = os.path.join(save_dir, f"captured_image_{image_count + 1}.jpg")
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