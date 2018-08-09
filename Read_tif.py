# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:02:34 2018

@author: PC1
"""


import tifffile as tiff #tif파일 불러오기 전용 import
import sys
import numpy as np
import os

sys.path.insert(0,r'''D:\download\solar\topo3\New Folder\VRT5_SRAD.tif''') # 다른 경로에 있는 파일 불러오기
sys.path.insert(0,r'''D:\download\solar\topo3\New Folder\VRT5_DEM.tif''')

class READ():
    def __init__(self):
        self.non_output = []
        self.val_output = []
        self.non_Output = []
        self.val_Output = []
        self.S = []
    
    def OUTPUT(self):
        
        file1 = []
        K2 = []
        K3 = []
        
        for i in range(0,113568):
            try:
                K=tiff.imread('D:/download/solar/topo3/New Folder/VRT5_SRAD.tif/VRT5_SRAD.tif.%d.tif'%i)
                K2 = K.reshape((900))
                K3 = np.sum(K2) / len(K2)
                file1 = [i,K,K3]
                if K.all() == False:
                    self.non_output.append(file1)    
                else:
                    self.val_output.append(file1)\
            except:
                print('Jump the removed file1.')
        for j1 in range(0,len(self.non.output)):
            self.S = self.non_output[j1][0]
            self.non_Output.append(self.S)
        for j2 in range(0,len(self.val_output)):
            S2 = self.val_output[j2][0]
            self.val_Output.append(S2)
            
        for y in self.non_Output:
            os.remove('D:/download/solar/topo3/New Folder/VRT5_SRAD.tif/VRT5_SRAD.tif.%d.tif'%y)
        
        return self.val_output
            
    def INPUT(self):
        print('start')
        
        files1 = []
        non_input = []
        val_input = []
        
        n3 = [x for x in range(0,113568)]
        for i2 in self.val_Output:
            n3.remove(i2)
        for m in range(0,113568):
            try:
                L=tiff.imread('D:/download/solar/topo3/New Folder/VRT5_SRAD.tif/VRT5_SRAD.tif.%d.tif'%m)
                files1 = [m,L]
                
                if m in n3:
                    non_imput.append(m)
                else:
                    val_input.append(files1)
            except:
                print('Jump the removed file2')
        for y2 in non_input:
            os.remove('D:/download/solar/topo3/New Folder/VRT5_SRAD.tif/VRT5_SRAD.tif.%d.tif'%y2)
            
        return val_input
    
if __name__ == "__main__":
    read = READ()
    read.OUTPUT()
    read.INPUT()
    
    # Remain the 100,550 files in input & output
        
        
    
    
