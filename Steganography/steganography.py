# steganography
# author: Justin Jiang
# date: Feb 18, 2023
# file: steganography.py creates methods to hide and encode messages into images by changing the image's RGB array
# input: input picture, output picture
# output: picture when decoded will return hidden message depending on selected decoding method

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None
        

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':

            while True:
                print("Enter a shift size: ")
                userShift = input()
                if userShift.isdigit() == True:
                    userShift = int(userShift)
                    break
                
            self.codec = CaesarCypher(shift = userShift)
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message+self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary
            # your code goes here
            # you may create an additional method that modifies the image array
            bin_count = 0
            
            for row in range(image.shape[0]):
                for col in range(image.shape[1]):
                    for count in range(3):
                        pixel = image[row][col][count]
                        if pixel % 2 != 0 and self.binary[bin_count] == "0":
                            if pixel == 255:
                                image[row][col][count] -= 1
                            else:
                                image[row][col][count] += 1
                        elif pixel % 2 == 0 and self.binary[bin_count] == "1":
                            image[row][col][count] += 1
                        bin_count += 1
                        if (bin_count == len(binary)):
                            bin_count = 0
                            break
                        

            cv2.imwrite(fileout, image)
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        #print(image) # for debugging      
        flag = True
        
        # convert into text
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':

            while True:
                print("Enter a shift size: ")
                userShift = input()
                if userShift.isdigit() == True:
                    userShift = int(userShift)
                    break
                
            self.codec = CaesarCypher(shift = userShift)
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            # your code goes here
            # you may create an additional method that extract bits from the image array
            binary_data = ''
            for row in range(image.shape[0]):
                for col in range(image.shape[1]):
                    for count in range(3):
                        binary_data += str(image[row][col][count] % 2)
            # update the data attributes:
            self.text = self.codec.decode(binary_data)
        
                          
        
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

if __name__ == '__main__':
    
    s = Steganography()

    s.encode('fractal.jpg', 'fractal.png', 'hello', 'binary')
    # NOTE: binary should have a delimiter and text should not have a delimiter
    assert s.text == 'hello'

    assert s.binary == '011010000110010101101100011011000110111100100011'

    
    s.decode('fractal.png', 'binary')
   
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'
    print('Everything works!!!')
   
