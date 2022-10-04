# VPRS-ITMO
Vehicle Plate Recognition System project

# Pipeline:
- Get frame from video stream (imitated)
- Find vehicles bounding boxes with YoloV4
- For each vehicle find number plate with OpenCV CascadeClassifier
- Plate text recognition with TF-ANPR
- Register vehicle arrival and department in DB

# Data:
- open datasets
- data scrapping