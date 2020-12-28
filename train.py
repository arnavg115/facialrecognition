
from PIL import Image
import tensorflow as tf
import os

from tensorflow import keras

train = tf.keras.preprocessing.image.ImageDataGenerator(1/255)

train_data = train.flow_from_directory('image_data/',target_size=(256,256),class_mode='binary',shuffle = True,batch_size=50)
numc = len(train_data.class_indices)
model = tf.keras.Sequential([tf.keras.layers.Conv2D(128,kernel_size = (2,2),activation='relu',input_shape = (256,256,3)),
                             tf.keras.layers.MaxPool2D(pool_size=(2,2)),
                             tf.keras.layers.Conv2D(64,kernel_size=(2,2),activation='relu'),
                             tf.keras.layers.Dropout(0.2),
                             tf.keras.layers.Flatten(),
                             tf.keras.layers.Dense(numc,activation='sigmoid')])
model.compile(optimizer='adam',loss='SparseCategoricalCrossentropy',metrics=['accuracy'])
model.fit(train_data,epochs=2)
print(model.summary)
model.save('model.h5')