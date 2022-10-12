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


