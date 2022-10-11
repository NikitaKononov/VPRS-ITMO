import cv2
import argparse
from detections import get_plates
from web_logging import HTML
import os
import datetime

parser = argparse.ArgumentParser(description='Car detection pipeline')
parser.add_argument('--vid_path', type=str, help='Video path', default='./carz.mp4')
parser.add_argument('--web_path', type=str, help='Path to web logs', default='./web/')
parser.add_argument('--results_path', type=str, help='Video path', default='./results/')

args = parser.parse_args()


if __name__ == '__main__':
    cap = cv2.VideoCapture(args.vid_path)
    idx = 0

    html = HTML(args.web_path, 'results')
    html.add_header('Detection results')

    if not os.path.exists(args.results_path):
        os.makedirs(args.results_path)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        img_path = args.results_path + 'image_{}.jpg'.format(idx)
        cv2.imwrite(img_path, frame)

        plate_bboxes, texts = get_plates(img_path)

        plates = []

        for i, pred in enumerate(plate_bboxes):
            cv2.rectangle(frame, (int(pred[0]), int(pred[1])), (int(pred[2]), int(pred[3])), (255, 0, 0), 5)

            plate_path = args.results_path + 'image_{}_plate_{}.jpg'.format(idx, i)
            plates.append(plate_path)
            cv2.imwrite(plate_path, cv2.resize(frame[int(pred[1]):int(pred[3]), int(pred[0]):int(pred[2])], (100, 25)))

        img_path_marked = args.results_path + 'image_marked_{}.jpg'.format(idx)
        cv2.imwrite(img_path_marked, frame)

        imgs = [img_path_marked]
        txts = ['']
        lnks = ['']

        for plate, text in zip(plates, texts[0]):
            imgs.append(plate)

            txts.append(text + ' Arrival ' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
            lnks.append('')

        html.add_images(imgs, txts, lnks)
        html.save()

        idx += 1