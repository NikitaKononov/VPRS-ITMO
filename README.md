# VPRS-ITMO
Vehicle Plate Recognition System project

Prepare:
```bash
conda create -n vprs python=3.6
conda activate vprs
pip3 install -r requirements.txt 
```
Run:
```bash
python demo.py
```

Resulting log webpage is in web/ folder

![img.png](misc/img.png)

# Experiments we've done:


- OpenCV cascade classifier to detect car bboxes: 
![img_1.png](misc/img_1.png)
- OpenCV cascade classifier to detect number plate bboxes:
![img_2.png](misc/img_2.png)
- Pytesseract to recognize number plate symbols:
<br>![img_3.png](misc/img_3.png)
<br>A867BG93<br>
- YoloV5 to detect number plate bboxes:
![img_4.png](misc/img_4.png)
- Nomeroff-net OCR to recognize plate number symbols:
<br>![img_5.png](misc/img_5.png) <br>B933XE93

# Experiments setup:


Hardware 
- CPU count: 1 Ryzen 4600H

All experiments were performed on a Ryzen 4600H CPU. For a faster recognition process, it is recommended to use the GPU

# Metrics


* IoU - metric, which changes in the range from 0 to 1, shows how much
  the so-called coverage area coincides with two objects (reference (ground true) and current).
  Ideal value 1. Used to determine the correct detection of cars and license plates

![img_6.png](misc/img_6.png)
  
# Prediction speed

- The processing time of one image, on which there are up to 5 cars,
on which license plates are visible, is approximately 5 seconds per CPU

- For real-time work, it is recommended to use the GPU
  
# Сhoosing the best model


1.  Detector we used YOLOv5


2.  Text recognition we used CRAFT


3. Training params:
  * Batch size: 16
  * Image size: 640x640
  * Epochs: 4

