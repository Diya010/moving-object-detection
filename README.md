# 🕵️‍♂️ Motion Detection Using OpenCV

This Python project uses OpenCV to detect motion from a webcam feed. It highlights moving objects in real-time and labels them with a status indicator.

## 📸 Features

- Real-time webcam video capture
- Motion detection using background subtraction
- Bounding boxes around detected movement
- Text overlay indicating motion status
- Graceful exit with key press (`q`)

## 🛠️ Technologies Used

- Python 3.x
- OpenCV (`cv2`)
- imutils
- time

## 🧠 How It Works

1. The webcam captures frames in real-time.
2. The first frame is used as a reference background.
3. New frames are compared with the background using absolute difference.
4. Thresholding and contour detection are used to find movement.
5. Bounding boxes are drawn around moving objects, and a "Moving Object Detected" message is displayed.

   



Uploading Testing rear collision.mp4…

