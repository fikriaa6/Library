import cv2
from fer import FER
 
# Initialize emotion detector
emotion_detector = FER()
 
# Start webcam feed
cap = cv2.VideoCapture(0)
 
# Loop to capture frames from the webcam
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame")
        break
 
    # Detect emotions in the frame
    emotions = emotion_detector.detect_emotions(frame)
    
    if emotions:
        # Get the first detected face's emotion data
        emotion_data = emotions[0]
        # Find the emotion with the highest confidence
        highest_confidence_emotion = max(emotion_data["emotions"], key=emotion_data["emotions"].get)
        
        # Get coordinates of the face and draw a rectangle around it
        (x, y, w, h) = emotion_data["box"]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
 
        # Display the emotion with the highest confidence on the frame
        cv2.putText(frame, highest_confidence_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
 
    # Display the frame with emotion detection
    cv2.imshow('Emotion Detector', frame)
 
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# Release webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()