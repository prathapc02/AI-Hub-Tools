import cv2

def start_recording():
    # Define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    # Start capturing video from default camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera")
        return

    while True:
        ret, frame = cap.read()

        # Check if frame is captured successfully
        if not ret:
            print("Error: Unable to capture frame")
            break

        # Write the frame to the video file
        out.write(frame)

        # Display the frame
        cv2.imshow('Frame', frame)

        # Check for 'q' key press to exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            print("Recording started...")
            while True:
                ret, frame = cap.read()
                out.write(frame)
                cv2.imshow('Frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    start_recording()

if __name__ == "__main__":
    main()
