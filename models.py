import numpy as np 
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.callbacks import ModelCheckpoint, LearningRateScheduler
#from tensorflow.keras import backend as keras
from tensorflow.keras import layers 


BINARY = 'binary'
CATEGORICAL = 'categorical'

__loss__ = {CATEGORICAL:'categorical_crossentropy', BINARY:'binary_crossentropy'}
__activation__ = {CATEGORICAL:'softmax', BINARY:'sigmoid'}
#_____________________________________________________________________________________________________________________________
#
#_____________________________________________________________________________________________________________________________




#_____________________________________________________________________________________________________________________________
#
#_____________________________________________________________________________________________________________________________
def resnet_unet(input_size,lr=1e-3, num_class=1, mode=BINARY):
    assert num_class>0, 'num class could not be 0'
    if mode==CATEGORICAL:
        assert num_class>1, "for categorical out_mode, num_class should be greater than 2"
    
    inputs = Input(shape=input_size)
    ### [First half of the network: downsampling inputs] ###
    # Entry block
    x =  Conv2D(32, 3, strides=2, padding="same")(inputs)
    x =  BatchNormalization()(x)
    x =  Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    # Blocks 1, 2, 3 are identical apart from the feature depth.
    for filters in [64, 128, 256]:
        x =  Activation("relu")(x)
        x =  SeparableConv2D(filters, 3, padding="same")(x)
        x =  BatchNormalization()(x)

        x =  Activation("relu")(x)
        x =  SeparableConv2D(filters, 3, padding="same")(x)
        x =  BatchNormalization()(x)

        x =  MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual =  Conv2D(filters, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x =  add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    ### [Second half of the network: upsampling inputs] ###

    for filters in [256, 128, 64, 32]:
        x =  Activation("relu")(x)
        x =  Conv2DTranspose(filters, 3, padding="same")(x)
        x =  BatchNormalization()(x)

        x =  Activation("relu")(x)
        x =  Conv2DTranspose(filters, 3, padding="same")(x)
        x =  BatchNormalization()(x)

        x =  UpSampling2D(2)(x)

        # Project residual
        residual =  UpSampling2D(2)(previous_block_activation)
        residual =  Conv2D(filters, 1, padding="same")(residual)
        x =  add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    # Add a per-pixel classification layer
    #outputs =  Conv2D(num_class, 3, activation=__activation__[mode], padding="same")(x)
    x =  Conv2D(num_class, 3, activation=None, padding="same")(x)
    outputs = Activation(__activation__[mode], dtype='float32')(x)

    # Define the model
    model = Model(inputs, outputs)

    model.compile(optimizer = Adam(lr = lr),
                  loss = __loss__[mode],
                  metrics = [
                      'accuracy', 
                       tf.keras.metrics.Precision(name='Precision'),
                       tf.keras.metrics.Recall(name='Recall')
                       ]
                  )
    
    #model.summary()

    return model




#_____________________________________________________________________________________________________________________________
#
#_____________________________________________________________________________________________________________________________
def resnet_unet2(input_size,lr=1e-3, num_class=1, mode=BINARY):
    assert num_class>0, 'num class could not be 0'
    if mode==CATEGORICAL:
        assert num_class>1, "for categorical out_mode, num_class should be greater than 2"
    
    inputs = Input(shape=input_size)
    ### [First half of the network: downsampling inputs] ###
    # Entry block
    x =  Conv2D(16, 3, strides=2, padding="same")(inputs)
    x =  BatchNormalization()(x)
    x =  Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    # Blocks 1, 2, 3 are identical apart from the feature depth.
    for filters in [32, 64, 128]:
        x =  Activation("relu")(x)
        x =  SeparableConv2D(filters, 3, padding="same")(x)
        x =  BatchNormalization()(x)

        x =  Activation("relu")(x)
        x =  SeparableConv2D(filters, 3, padding="same")(x)
        x =  BatchNormalization()(x)

        x =  MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual =  Conv2D(filters, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x =  add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    ### [Second half of the network: upsampling inputs] ###

    for filters in [128, 64, 32, 16]:
        x =  Activation("relu")(x)
        x =  Conv2DTranspose(filters, 3, padding="same")(x)
        x =  BatchNormalization()(x)

        x =  Activation("relu")(x)
        x =  Conv2DTranspose(filters, 3, padding="same")(x)
        x =  BatchNormalization()(x)

        x =  UpSampling2D(2)(x)

        # Project residual
        residual =  UpSampling2D(2)(previous_block_activation)
        residual =  Conv2D(filters, 1, padding="same")(residual)
        x =  add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    # Add a per-pixel classification layer
    #outputs =  Conv2D(num_class, 3, activation=__activation__[mode], padding="same")(x)
    x =  Conv2D(num_class, 3, activation=None, padding="same")(x)
    outputs = Activation(__activation__[mode], dtype='float32')(x)

    # Define the model
    model = Model(inputs, outputs)

    model.compile(optimizer = Adam(lr = lr),
                  loss = __loss__[mode],
                  metrics = [
                      'accuracy', 
                       tf.keras.metrics.Precision(name='Precision'),
                       tf.keras.metrics.Recall(name='Recall')
                       ]
                  )
    
    #model.summary()

    return model

#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------

#_____________________________________________________________________________________________________________
#
#_____________________________________________________________________________________________________________



if __name__=='__main__':
    model = resnet_cnn( (128,800,3), num_class=5, mode=BINARY, fine_tune_layer=100 )
    
    end = True