#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:49:46 2018

@author: dy
"""
import numpy as np
from PIL import Image
import skimage.io
import shutil  
import os
import sys

from inference_dy_3 import parse_arguments, main_dy

#import matplotlib.pyplot as plt
#from skimage import measure,draw

original_path = '/home/dy/dy/smart_design/cluster_0521/mouse/'
output_folder = '/home/dy/dy/smart_design/out_dy/mouse/'
bw_file_path = '/home/dy/dy/smart_design/out_bw/mouse/'
new_file_path = '/home/dy/dy/smart_design/unreasonable'              ##    delete

isExists=os.path.exists(bw_file_path)
if not isExists:
    os.makedirs(bw_file_path)

file_images = []

main_dy(parse_arguments(sys.argv[1:]))

for f in os.listdir(original_path):
    if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png'):
        file_images.append(f)

os.chdir(original_path)
for file in file_images:
    if file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.png'):
    
        img_original = Image.open(file)
        r,g,b = img_original.split()

        img = Image.open(output_folder+file).convert("L")
        
        imgs = skimage.io.imread(output_folder + file)
        ttt = np.mean(imgs)
        
        WHITE, BLACK = 255, 0
        
        img = img.point(lambda x: WHITE if x > ttt else BLACK)
        img = img.convert('1')
        img.save(bw_file_path+file)
    
######   find edges
    #    contours = measure.find_contours(img, 0.5)
    #    
    #    fig, (ax0,ax1) = plt.subplots(1,2,figsize=(8,8))
    #    ax0.imshow(img,plt.cm.gray)
    #    ax1.imshow(img,plt.cm.gray)
    #    for n, contour in enumerate(contours):
    #        ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
    #    ax1.axis('image')
    #    ax1.set_xticks([])
    #    ax1.set_yticks([])
    #    plt.show()
    
        width, height = img.size  
        pix = img.load()
        
        pix_r = r.load()
        pix_g = g.load()
        pix_b = b.load()
        
        a = [0]*256 
        zero_sum = 0
        white_sum = 0
    
        for w in range(width):  
            for h in range(height):  
                p = pix[w,h]
                p_r = pix_r[w,h]
                p_g = pix_g[w,h]
                p_b = pix_b[w,h]
                if p == 0 :
                    zero_sum = zero_sum + 1
                    if (p_r > 245 and p_g > 245 and p_b > 245):
                        white_sum = white_sum + 1
        perc = white_sum/zero_sum
        if perc <0.1:
            print(file + ' was removed \n')
#            shutil.move(file,new_file_path)
            os.remove(file)
        elif white_sum < 10000:
            print(file + ' was removed \n')
#            shutil.move(file,new_file_path)
            os.remove(file)
        print (zero_sum,white_sum,perc)    #长度256,a保存的分别是颜色范围0-255出现的次数
