# Import necessary libraries
import cv2  # OpenCV library for computer vision tasks
import numpy as np  # NumPy for numerical operations, commonly used in image processing


# Load pre-trained Haar Cascade classifier for face detection
# Haar Cascade classifiers are pre-trained models that can detect specific objects
# The XML file contains the trained model for detecting faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Start video capture from the webcam
# VideoCapture(0) accesses the default webcam. If you have multiple cameras, you can change the index.
video_capture = cv2.VideoCapture(0)


# Check if the video capture object was successfully created
# If not, print an error message and exit the program
if not video_capture.isOpened():
    print("Error: Could not access the webcam.")
    exit()


# Main loop to process each video frame
while True:
    # Capture a frame-by-frame from the webcam
    # ret is a boolean indicating if the frame was read successfully
    # frame is the actual image captured from the webcam
    ret, frame = video_capture.read()


    # If the frame was not read correctly, print an error message and exit the loop
    if not ret:
        print("Error: Unable to read frame from webcam.")
        break


    # Convert the captured frame to grayscale
    # Face detection works more effectively on grayscale images as it simplifies the data
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Detect faces in the grayscale image
    # detectMultiScale() detects objects in an image, here it detects faces
    # scaleFactor compensates for faces appearing at different sizes
    # minNeighbors specifies the minimum number of neighbors a rectangle should have to retain it
    # minSize specifies the minimum size of the detected face
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    # Draw rectangles around detected faces
    # Loop through the list of detected faces and draw rectangles on the original frame
    # (x, y) is the top-left corner of the rectangle, (x+w, y+h) is the bottom-right corner
    # (255, 0, 0) specifies the color of the rectangle in BGR format (blue here)
    # Thickness of the rectangle is set to 2 pixels
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw a blue rectangle around the face


    # Display the resulting frame with detected faces highlighted
    # 'Face Detection' is the title of the window displaying the frame
    cv2.imshow('Face Detection', frame)


    # Wait for 1 millisecond and check if the 'q' key was pressed
    # If 'q' is pressed, break the loop and exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the video capture object to free up the webcam
# Close all OpenCV windows to clean up resources
video_capture.release()
cv2.destroyAllWindows()



