import time

import requests
import cv2
import numpy as np
from PIL import Image

start = time.perf_counter()

size = (1200, 1200)

def process_image(img_url):
    print('Processing image')
    image = requests.get(img_url)
    img = cv2.imdecode(np.asarray(bytearray(image.content)), cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(img)
    print('Processed image', img)
    