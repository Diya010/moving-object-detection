import cv2
import time
import imutils

# Initialize webcam
cam = cv2.VideoCapture(0)
time.sleep(1)

# Check if camera opened successfully
if not cam.isOpened():
    print(" Error: Cannot access the camera.")
    exit()

first_frame = None
area = 500

while True:
    ret, img = cam.read()
    if not ret or img is None:
        print(" Failed to grab frame from camera.")
        break

    text = "Normal"
    img = imutils.resize(img, width=800)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gaussian
        continue

    img_diff = cv2.absdiff(first_frame, gaussian)
    thresh = cv2.threshold(img_diff, 30, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for contour in cnts:
        if cv2.contourArea(contour) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object Detected"

    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 255, 0), 2)

    cv2.imshow("Camera Feed", img)

    key = cv2.waitKey(10)
    if key == ord("q"):
        break

# Release and cleanup
cam.release()
cv2.destroyAllWindows()
