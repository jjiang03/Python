# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes
import os

image = cv2.imread("redbox.jpg")
'''
bin_count = 0
for row in range(image.shape[0]):
    for col in range(image.shape[1]):
        for count in range(3):
            value = image[row][col][count]

        
for pos, i in np.ndenumerate(image):
    value = image[pos[0]][pos[1]][pos[2]]
    print(value)
    
binary_data = ''
for i in np.nditer(image):
    binary_data += str(i % 2)
print(binary_data)
print("________")
p = ""
for row in range(image.shape[0]):
    for col in range(image.shape[1]):
        for count in range(3):
            p += str(image[row][col][count] % 2)
print(p)
'''  
freq = {}
for i in "hello":
    if i in freq.keys():
        freq[i] += 1
    else:
        freq[i] = 1
    
print(freq)
