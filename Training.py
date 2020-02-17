# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:18:06 2019

@author: Krishna Chandra
"""



import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split

import keras
from keras.models import Model, load_model
from keras.layers import Input ,BatchNormalization , Activation 
from keras.layers.convolutional import Conv2D, UpSampling2D
from keras.layers.pooling import MaxPooling2D
from keras.layers.merge import concatenate
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import optimizers 
from sklearn.model_selection import train_test_split


import data_preprocessing as process
import Model
import plots
import Metrics

# Setting the path
Path='G:/Multiple Scelerosis/Data Sets/MS segmentation challenge using a data management and processing infrastructure/Pre-processed'



# Loading all the 5 different modalities of each MRI Scan of all 15 different patients and 1st rater Manual Segmentation
# file_indices = {0,1,2,10,11,3}

X_Dp      =   process.modality(Path,0)
X_Flair   =   process.modality(Path,1)
X_Gado    =   process.modality(Path,2)
X_T1      =   process.modality(Path,10)
X_T2      =   process.modality(Path,11)
Y_Manual  =   process.modality(Path,3)

# Removing the null samples and concatenating the 5 modalities along the 3rd dimension
X, Y = process.remove_null_samples(X_Dp, X_Flair, X_Gado, X_T1, X_T2, Y_Manual)

# Storing the data as numpy arrays 
process.store_data(X,Y)

# Splitting the Whole data into Training and Testing data
X_train , X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15, random_state=32)

# Loding the Light weighted CNN
model = Model.model(input_shape = (256,256,5))
model.summary()

# Compiling the model 
Adam=optimizers.adam(lr=0.001)
model.compile(optimizer=Adam, loss='binary_crossentropy', metrics=['accuracy',Metrics.dice_coef,Metrics.precision,Metrics.sensitivity,Metrics.specificity])

# Fitting the model over the data
history = model.fit(X_train,Y_train,batch_size=32,epochs=2,validation_split=0.20,verbose=1,initial_epoch=0)

# Saving the model
model.save('Modified_UNet.h5')

# Evaluating the model on the training and testing data 
model.evaluate(x=X_train, y=Y_train, batch_size=32 , verbose=1, sample_weight=None, steps=None)
model.evaluate(x=X_test, y=Y_test, batch_size=32, verbose=1, sample_weight=None, steps=None)

# Plotting the Graphs of Accuracy, Dice_coefficient, Loss at each epoch on Training and Testing data
plots.Accuarcy_Graph(history)
plots.Dice_coefficient_Graph(history)
plots.Loss_Graph(history)












