import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
import os

# safer absolute path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "skin_model.h5")

model = tf.keras.models.load_model(MODEL_PATH)

class_names = ["Eczema", "Psoriasis", "Acne"]

def predict_skin(image_path: str):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return predicted_class, confidence