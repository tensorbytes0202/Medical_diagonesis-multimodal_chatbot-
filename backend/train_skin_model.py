import tensorflow as tf
from tensorflow.keras import layers, models
import os

IMG_SIZE = 128
BATCH_SIZE = 32

dataset = tf.keras.preprocessing.image_dataset_from_directory(
    r"C:\\Users\\Aditya Sikarwar\\Downloads\\skin_dataset",
    image_size=(128, 128),
    batch_size=32
)

class_names = dataset.class_names

model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    
    layers.Conv2D(32, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(class_names), activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(dataset, epochs=10)

model.save("app/models/skin_model.h5")