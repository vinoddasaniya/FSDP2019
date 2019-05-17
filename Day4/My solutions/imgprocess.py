# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:59:40 2019

@author: kk
"""

"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""

from PIL import Image
import os
img1 = Image.open("sample1.jpg")
print(img.size)
print(img.greyscale)
img_rotate = img.transpose(Image.ROTATE_90)
small_im = img.resize((300, 150), resample=Image.BICUBIC)
crop_im = img.crop(box=(160, 20, 204, 164))
img.thumbnail((75, 75))
img.save('thumb_sample1.jpg')

