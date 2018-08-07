# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:02:34 2018

@author: PC1
"""


import tifffile as tiff #tif파일 불러오기 전용 import
import sys
#import numpy as np

sys.path.insert(0,r'''D:\download\solar\topo3\New Folder\VRT2_SRAD.tif''') # 다른 경로에 있는 파일 불러오기

class READ():
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

K = []        
file1 = []
file2 = []


for i in range(0,10000):
    K=tiff.imread('D:/download/solar/topo3/New Folder/VRT2_SRAD.tif/VRT2_SRAD.tif.%d.tif'%i)
    S = 0
    if K.any() == S:
        file2.append(K)    
    else:
        file1.append(K)
    
        
        
    
    #K = tiff.imread('split_DEM.tif.i.tif')
    
#A = tiff.imread('D:/download/solar/topo3/New Folder/ITRF_DEM_ProjectRaster1_Proj11.tif')
#tiff.imshow(K)

'''
# 탐색 시, 특정 디렉토리 제외하기
import os
pwd = 'path'
for path, dirs, files in os.walk(pwd):
    dir[:] = [dir for dir in dirs if dir != "etc"]

#탐색 시, 특정 파일만 추려내기
for path, dirs, files in os.walk(pwd):
    for file in files:
        if os.path.splitext(file)[1].lower()  == '.pyc':
            print('pyc file' + file)
'''
