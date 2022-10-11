import cv2
from nomeroff_net import pipeline
from nomeroff_net.tools import unzip


def get_cars(img):
    cars_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
    cars = cars_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)
    return cars


def get_plates(img_path):
    number_plate_detection_and_reading = pipeline("number_plate_detection_and_reading", image_loader="opencv")

    (images, images_bboxs,
     images_points, images_zones, region_ids,
     region_names, count_lines,
     confidences, texts) = unzip(number_plate_detection_and_reading([img_path]))

    return images_bboxs[0], texts
