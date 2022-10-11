import cv2
from detections import get_cars

cap = cv2.VideoCapture('carz.mp4')
idx = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imwrite('./results/image_{}.jpg'.format(idx), frame)

    plate_bbox = get_cars(frame)
    print(plate_bbox)

    # for x, y, w, h in plate_bbox:
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

    cv2.imwrite('{}.jpg'.format(idx), frame)

    idx += 1