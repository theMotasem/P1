# -*- coding: utf-8 -*-
"""p1_face_blurring.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qYtDHEzy36GDsdp644dur0YyMFA8PraI
"""

import cv2

image_path = '/content/RT00.jpg'
image = cv2.imread(image_path)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    face_roi = image[y:y+h, x:x+w]
    
    face_roi = cv2.GaussianBlur(face_roi, (25, 25), 0)
    
    image[y:y+h, x:x+w] = face_roi

cv2.imwrite('output_image.jpg', image)

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
img = Image.open('output_image.jpg')
img_arr = np.array(img)
plt.imshow(img_arr)
plt.show()

