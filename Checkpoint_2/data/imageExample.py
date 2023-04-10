#@title Imports

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import os
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

#@title Normalize Saturation and Value:
def normalize_saturation_value(input_img):
    # Convert the image from BGR to HSV color space
    hsv_image = image.rgb_to_hsv(input_img)
    #hsv_image = cv2.cvtColor(input_img, cv2.COLOR_BGR2HSV)

    # Split the HSV image into separate channels
    h, s, v = cv2.split(hsv_image)

    # Normalize the saturation and value channels
    s = np.uint8(np.clip((s * 1.2), 0, 255))
    v = np.uint8(np.clip((v * 1.2), 0, 255))

    # Merge the normalized channels back into an HSV image
    hsv_image = cv2.merge([h, s, v])

    # Convert the HSV image back to BGR color space
    output_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    return output_image