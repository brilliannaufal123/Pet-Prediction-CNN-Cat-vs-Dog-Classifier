import os

# Set your exact space folder name
repo_dir = 'pet-prediction-cnn'

# Create requirements.txt
with open(os.path.join(repo_dir, 'requirements.txt'), 'w') as f:
    f.write("tensorflow\ngradio\nnumpy\npillow")

# Create app.py with clean English comments
app_code = """import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model('model_hewan.h5')
labels = ['Cat', 'Dog']

def predict_image(image):
    image = image.resize((128, 128))
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_class = labels[1] if prediction[0][0] > 0.5 else labels[0]
    return f"Prediction: {predicted_class}"

# Build Gradio interface
interface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Cat vs Dog Classifier 🐱🐶",
    description="Upload an image to predict whether it is a Cat or a Dog."
)

interface.launch()
"""

with open(os.path.join(repo_dir, 'app.py'), 'w') as f:
    f.write(app_code)

print("Deployment files successfully created inside 'pet-prediction-cnn'!")
