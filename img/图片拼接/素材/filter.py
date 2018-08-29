#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:36:29 2018

@author: lee
"""

import os
from PIL import Image
from collections import Counter
import re
import pandas as pd

file_list = []
path_list = os.listdir('./')
##筛选都有的icon
'''
for path in path_list:
    if '_ic_' in path:
        print(path)
        files = os.listdir('./'+path)
        file_list.extend(files)
        print(len(files))

a = pd.Series(Counter(file_list))
icons = {}
icon_list = list(a[a==6].index)
for i in icon_list:
    j = re.split('.png',i)[0]
    print(j)
    icons[j] = i
    
icons = str(icons)
    
with open("./icon_list.txt","w") as f:
    f.write(icons)
'''

filename = r'./Gold Silk Rose Theme/auto_180x120.jpg'

def get_size(file):
    img = Image.open(file)
    imgSize = img.size #图片的长和宽
    maxSize = max(imgSize) #图片的长边
    minSize = min(imgSize) #图片的短边
    return maxSize,minSize

def define(file):
    imgSize = get_size(file)
    if imgSize == (180,120):
        print('1')
    
