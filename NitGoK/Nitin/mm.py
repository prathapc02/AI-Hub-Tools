import cv2
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import img_to_array

# Load the face detector
face_classifier = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

# Load the model using tf.keras.models.load_model
try:
    classifier = tf.keras.models.load_model('model.h5')
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Define emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Start video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Process video frames
while True:
    # Capture frame from video
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Process detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255,255), 2)

        # Extract the region of interest (ROI) in grayscale
        roi_gray = gray[y:y + h, x:x + w]

        # Resize the ROI to the input size expected by the model (48x48)
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        # Ensure there is a valid region of interest
        if np.sum([roi_gray]) != 0:
            # Normalize the ROI and convert it to an array
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            # Predict the emotion using the classifier
            prediction = classifier.predict(roi)[0]
            max_index = np.argmax(prediction)
            label = emotion_labels[max_index]

            # Display the predicted emotion on the frame
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            # Display "No Faces" if there is no valid ROI
            cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame in a window
    cv2.imshow('Emotion Detector', frame)

    # Exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up: release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
