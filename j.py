import cv2

# Open the default camera (0 is usually the built-in webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Press 's' to take a photo, 'q' to quit")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting...")
        break

    # Display the frame
    cv2.imshow('Camera', frame)

    # Wait for key press
    key = cv2.waitKey(1)
    if key == ord('s'):  # Press 's' to save the photo
        cv2.imwrite('photo.jpg', frame)
        print("Photo saved as photo.jpg")
    elif key == ord('q'):  # Press 'q' to quit
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()