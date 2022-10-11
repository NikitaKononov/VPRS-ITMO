import cv2
import argparse
from detections import get_plates
from web_logging import HTML
import os

parser = argparse.ArgumentParser(description='Car detection pipeline')
parser.add_argument('--vid_path', type=str, help='Video path', default='./carz.mp4')

args = parser.parse_args()


if __name__ == '__main__':
    cap = cv2.VideoCapture(args.vid_path)
    idx = 0

    html = HTML('./web/', 'results')
    html.add_header('Detection results')

    if not os.path.exists('./results/'):
        os.makedirs('./results/')

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        img_path = './results/image_{}.jpg'.format(idx)
        cv2.imwrite(img_path, frame)

        plate_bboxes, texts = get_plates(img_path)

        plates = []

        for i, pred in enumerate(plate_bboxes):
            print(pred)
            cv2.rectangle(frame, (int(pred[0]), int(pred[1])), (int(pred[2]), int(pred[3])), (255, 0, 0), 5)

            plate_path = './results/image_{}_plate_{}.jpg'.format(idx, i)
            plates.append(plate_path)
            cv2.imwrite(plate_path, frame[int(pred[1]):int(pred[3]), int(pred[0]):int(pred[2])])

        img_path_marked = './results/image_marked_{}.jpg'.format(idx)
        cv2.imwrite(img_path_marked, frame)

        imgs = [img_path_marked]
        txts = ['']
        lnks = ['']

        print(plates)
        print(texts[0])

        for plate, text in zip(plates, texts[0]):
            imgs.append(plate)
            txts.append(text)
            lnks.append('')

        html.add_images(imgs, txts, lnks)
        html.save()

        idx += 1