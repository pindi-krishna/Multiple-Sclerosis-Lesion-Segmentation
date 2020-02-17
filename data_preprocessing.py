# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:34:44 2019

@author: Krishna Chandra
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 12:32:05 2019

@author: Krishna
"""
# Importing neccessary packages
import tensorflow as tf
import numpy as np
import os
import nibabel as nib
import cv2 as cv
import matplotlib.pyplot as plt
    
def modality(Path,index):
    X = []
    p=os.listdir(Path) 

    for i in p[:14]:                                                                      # Loading all the folders in the given path
        q = os.listdir(os.path.join(Path,i))     

        x = nib.load(os.path.join(Path,i,q[index]))         
        f = x.get_fdata()
        f = np.asarray(f,'float32')
        
        for j in range(f.shape[2]):                                                        # Processing the MRI Scan in the axial view
            _slice = cv.resize(f[:,:,j],(256,256),interpolation=cv.INTER_NEAREST)             # Resizing the slice to the shape(256,256)
            if(index != 3 and np.sum(_slice) != 0 ):                                           # To check whether the slice is null or not
                _slice = _slice / (np.max(_slice) + 0.00001)                               # Normalization
                _slice = (_slice - np.mean(_slice) + 0.00001) / (np.std(_slice) + 0.00001) # Standardization
            elif(index == 3):   # if index = 3, Then it is output mask and we don't normalize or standardize it 
                _slice = np.array(_slice)
                _slice[_slice > 0] = 1.0
            _slice = _slice.T
            _slice = _slice[:,:,np.newaxis]
            X.append(_slice)
    return X

# Removing the null samples as it contains no information
def remove_null_samples(X_Dp, X_Flair, X_Gado, X_T1, X_T2, Y_Manual): 
     
    X=[]
    Y=[]
    
    for i in range(len(X_Dp)):        
        final_slice = np.concatenate((X_Dp[i],X_Flair[i],X_Gado[i],X_T1[i],X_T2[i]), axis = -1)
        if(np.sum(final_slice) != 0):        # checking whether the final slice is empty or not             
            X.append(final_slice)
            Y.append(Y_Manual[i])
 
#   Converting the list into array  
    X=np.array(X,dtype='float32')
    Y=np.array(Y,dtype='float32')
    
    return X,Y

#   To store the data in numpy format    
def store_data(X,Y):
    np.save("X.npy",X)
    np.save("Y.npy",Y)


        


    

    
