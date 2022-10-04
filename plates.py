import cv2


def get_plate(img):
    cascade = cv2.CascadeClassifier('./rus_plates.xml')
    plate_bbox = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)
    return plate_bbox[0][0], plate_bbox[0][1], plate_bbox[0][2], plate_bbox[0][3]

