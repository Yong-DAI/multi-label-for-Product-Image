#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:03:07 2018

@author: dy
"""
import numpy as np
import scipy.misc
import os  
from PIL import Image


def imread(path, grayscale = False):
  if (grayscale):
    return scipy.misc.imread(path, flatten = True).astype(np.float)
  else:
    return scipy.misc.imread(path).astype(np.float)


path = './output-3'      ####   headset   handband   watch   VR

num = 1
for root, dirs, files in os.walk(path):  
    if len(dirs) == 0:  
        for i in range(len(files)):  
            if files[i][-3:] == 'jpg':  
                file_path = root+'/'+files[i]  
                imreadImg = imread(file_path)
                if imreadImg.shape[-1] !=3:
                    print(imreadImg.shape[-1])
                    print(file_path)
                    ######   modify
                    resave_in_correct = Image.open(file_path).convert('RGB').save(file_path)
                    num = num +1
                    ######   delete
#                    os.remove(file_path)
        print ('the number of incorrect images is %d'%num)


#imreadImg = imread(path+'/13129610215_3.jpg')
#print(imreadImg.shape[-1])