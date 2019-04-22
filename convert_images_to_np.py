import tensorflow as tf
import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
from PIL import Image
import glob
import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array #load_im

'''
@author
        Joshua Carney  [Carneyj4@uab.edu]
        Jeremy Blackburn [blackburn@uab.edu]
@Topic
        Meme-Generator
        A GAN that trains on given images and will generate 
        a new meme, based off the inputted memes. 
@Citations
        NVIDIA: 
        UCLAACM:

'''
def main():
    folder = input('What is the full file path to your image files?')
    np_folder = input('Put the full file path for where you want your np files to be saved')
    _glob =  [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    image_width = 28
    image_height = 28

    channels = 3
    nb_classes = 1

    dataset = np.ndarray(shape=(1000, channels, image_height, image_width),
                        dtype=np.float32)
    success, failure, i = 0, 0, 0
    failed_files = list()
    for files in _glob:
        i+=1

        try:
            os.chdir(folder)
            x = cv2.imread(files)#, cv2.IMREAD_GRAYSCALE)#,mode='RGB')
            x = cv2.resize(x, (28, 28))
            bgr_x = cv2.cvtColor(x, cv2.COLOR_RGB2BGR)
            gray_x = cv2.cvtColor(bgr_x, cv2.COLOR_BGR2GRAY)
            x = gray_x.reshape((1,28,28))
            os.chdir(np_folder)
            np.save(files.split('.')[0], gray_x)
            #plt.imshow(gray_x, cmap='gray')
            #plt.show()
            print(f"Success {files}")
            success += 1
        except:
            print(f'Failed {files}')
            failed_files.append(files)
            failure += 1
            continue
    print(f'Successful Conversions: {success}\nFailed Conversions: {failure}')
    print(failed_files)

main()
