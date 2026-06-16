import cv2
import time

print('OpenCV version:', cv2.__version__)
for i in range(3):
    print(f'Trying camera index {i}...')
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print('  Cannot open camera index', i)
        continue
    ret, frame = cap.read()
    if not ret:
        print('  Opened but cannot read frame')
        cap.release()
        continue
    print('  Success: captured frame from index', i)
    cv2.imwrite(f'test_cam_{i}.jpg', frame)
    cap.release()
    break
else:
    print('No camera could be opened. Check device drivers or if another app uses the camera.')

# Sleep briefly to ensure file flush
time.sleep(0.2)
print('Done')
