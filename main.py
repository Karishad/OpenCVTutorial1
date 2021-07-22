# Kieron Yin
# 7/22/2021
# https://www.geeksforgeeks.org/introduction-to-opencv/
# Practice introduction into OpenCV

import cv2
# Reading the image file labeled 'image.png'
image = cv2.imread('image.png')

# Section 1 - Reading Image dimentions
# Extracts the height and width of 'image.png'
h, w = image.shape[:2]
# Display the height and width of 'image.png'
print("Height = {}, Width = {}".format(h, w))

# Section 2 - Cropping image
crop = image[109 : 500, 200 : 700]
