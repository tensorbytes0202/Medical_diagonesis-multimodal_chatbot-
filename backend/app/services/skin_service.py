import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

MODEL_PATH = os.path.join("app", "models", "skin_model.h5")
model = tf.keras.models.load_model(MODEL_PATH)

class_names = [
    "Atopic Dermatitis",
    "Herpes",
    "Lyme disease",
    "Poison Ivy",
    "Psoriasis",
    "Rosacea"
]

def predict_skin(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).resize((128,128))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = float(np.max(predictions))

    return predicted_class, confidence