import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

# Initialize the face cascade and the dataset path
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
dataset_path = "./face_dataset/"

# Initialize the global variables
cap = None
face_data = []
root = Tk()

def capture_faces():
    global cap, face_cascade, dataset_path, root, face_data

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Create a new window to enter the name
    name_window = Toplevel(root)
    name_window.title("Enter Name")
    name_window.geometry("300x100")
    name_window.configure(bg='#000000')

    # Add a label and entry for the name
    name_label = Label(name_window, text="Enter Name:", fg="white", bg="#000000")
    name_label.pack()

    name_entry = Entry(name_window)
    name_entry.pack()

    def start_capture():
        global face_data

        # Retrieve the name from the entry field
        name = name_entry.get()
        
        # Define the dataset path and file name
        file_name = name + ".npy"

        # Initialize an empty list for face data
        face_data = []

        # Define the number of photos to capture
        photos_to_capture = 200
        photos_captured = 0

        while True:
            # Read frames from the camera
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame from the camera.")
                break

            # Convert frame to grayscale and detect faces
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

            # Sort faces by size and process the largest face
            faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)

            for face in faces[:1]:
                x, y, w, h = face
                offset = 5
                face_offset = frame[y - offset:y + h + offset, x - offset:x + w + offset]
                face_selection = cv2.resize(face_offset, (100, 100))

                if photos_captured < photos_to_capture:
                    # Append the face selection to face_data
                    face_data.append(face_selection)
                    photos_captured += 1
                    print(f"Photo {photos_captured} captured")

                # Display the face selection and mark face in the frame
                cv2.imshow("face selection", face_selection)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the frame with marked face
            cv2.imshow("faces", frame)

            # Break the loop if 'q' is pressed or photos_to_capture is reached
            key_pressed = cv2.waitKey(1) & 0xFF
            if key_pressed == ord('q') or photos_captured >= photos_to_capture:
                break

        # Save the face data as a numpy file if photos were captured
        if photos_captured > 0:
            face_data = np.array(face_data)
            face_data = face_data.reshape((face_data.shape[0], -1))
            np.save(dataset_path + file_name, face_data)
            print(f"Dataset saved at: {dataset_path + file_name}")

        # Calculate accuracy
        accuracy = (photos_captured / photos_to_capture) * 100

        # Print the accuracy
        print(f"Accuracy of face capture for {name}: {accuracy:.2f}%")

        # Plot the accuracy using Matplotlib
        plt.figure()
        plt.bar(['Accuracy'], [accuracy])
        plt.title(f'Face Capture Accuracy for {name}')
        plt.ylabel('Accuracy (%)')
        plt.ylim(0, 100)
        plt.show()

        # Release the camera and close windows
        cap.release()
        cv2.destroyAllWindows()

        # Close the name window
        name_window.destroy()

    # Create a button in the name window to start capture
    start_button = Button(name_window, text="Start Capture", command=start_capture, bg="#808080", fg="#262626")
    start_button.pack()

capture_faces()
root.mainloop()
