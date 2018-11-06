#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:49:46 2018

@author: dy
"""
import numpy as np
from PIL import Image
import skimage.io
#import shutil  
import os
import sys

from inference_dy_6 import parse_arguments, main_dy

#import matplotlib.pyplot as plt
#from skimage import measure,draw

output_folder = '/home/dy/dy/smart_design/out_dy_6/mouse/'
bw_file_path = '/home/dy/dy/smart_design/out_bw_6/mouse/'

isExists=os.path.exists(bw_file_path)
if not isExists:
    os.makedirs(bw_file_path)

file_images = []

main_dy(parse_arguments(sys.argv[1:]))

for f in os.listdir(output_folder):
    if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png'):
        file_images.append(f)
        
###     save as the original name     ,so this is ok althrough reading not in order
os.chdir(output_folder)
for file in file_images:
    if file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.png'):

        img = Image.open(output_folder+file).convert("L")                                      
        
        imgs = skimage.io.imread(output_folder + file)
        ttt = np.mean(imgs)

        WHITE, BLACK = 255, 0
        
        img = img.point(lambda x: WHITE if x > ttt else BLACK)
        img = img.convert('1')
        img.save(bw_file_path+file)
        print( file +' has saved')

