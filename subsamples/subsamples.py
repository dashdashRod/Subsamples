import cv2
import numpy as np

import cv2

def To_422(image):
    new_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    s = new_image.shape
    for x in range(s[1]):
        for y in range(0, s[0], 2):
            if y + 1 < s[0]:
                new_image[y + 1, x][1] = new_image[y, x][1]
                new_image[y + 1, x][2] = new_image[y, x][2]
    return new_image

def To_440(image):
    new_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    s = new_image.shape
    for x in range(0, s[1], 2):
        for y in range(s[0]):
            if x + 1 < s[1]:
                new_image[y, x + 1][1] = new_image[y, x][1]
                new_image[y, x + 1][2] = new_image[y, x][2]
    return new_image

def To_420(image):
    new_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    s = new_image.shape
    for x in range(0, s[1], 2):
        for y in range(0, s[0], 2):
            if x + 1 < s[1]:
                new_image[y, x + 1][1] = new_image[y, x][1]
                new_image[y, x + 1][2] = new_image[y, x][2]
                new_image[y + 1, x][1] = new_image[y, x][1]
                new_image[y + 1, x][2] = new_image[y, x][2]
                new_image[y + 1, x + 1][1] = new_image[y, x][1]
                new_image[y + 1, x + 1][2] = new_image[y, x][2]
    return new_image

def To_411(image):
    new_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    s = new_image.shape
    for x in range(s[1]):
        for y in range(s[0]):
            if y % 4 != 0:
                new_image[y, x, 1] = new_image[y - 1, x, 1]
                new_image[y, x, 2] = new_image[y - 1, x, 2]
    return new_image