# Pet-Prediction-CNN-Cat-vs-Dog-Classifier

An interactive, end-to-end Deep Learning web applications built from scratch using a Convolutional Neural Networks (CNN) to classify images of cats and dogs, deployed seamlessly to production.

## Project Overview
* **Year Accomplished:** 2026
* **Deployment Link:** [Live Hugging Face Space](https://huggingface.co/spaces/brilliannaufal06/pet-prediction-cnn)

<img width="2879" height="1440" alt="image" src="https://github.com/user-attachments/assets/aa3a9218-da89-4182-b12d-94cd74cc92fb" />


## Behind the Making

### The Problem
In Computer Vision, binary image classification serves as the foundational stepping stone for more complex recognition system. However, real-world images datasets are notorious for being clustered with corrupted bytes headers and broken metadata that break model pipelines during runtime. I wanted to build a clean, end-to-end pipeline that handles automated data validation, custom-model training, and immediate web deployment.

### The Strategy & Tech Stack
* **Framework:** Python, TensorFlow / Keras (Sequential API)
* **Environment:** Google Colab (T4 GPU Acceleration)
* **Interface & Deployment:** Gradio, Hugging Face Spaces (Git LFS tracking)
* **The Engineering Process:**
  1. **Data Sanitization:** Created a custom byte-header scanning script to programmatically inspect the dataset.
  2. **Feature Extraction:** Built a CNN architecture using stacking pairs of 'Conv2D' and 'MaxPooling2D' layers to capture low-to-high-level visual features.
  3. **Classification:** Flattened the spatial layers into a dense network utilizing a 'sigmoid' activation function to compute binary class probabilities.
 
### The Results
A fully functional, containerized web application where anyone can drag and drop an image of a pet and receive instant classification results.

---

## Engineering Insights & Work in Progress (WIP)

Here are the core experiments from this build:

### 1. Data Cleaning (Handling the 499 Bottlenecks)
During the initial training runs, the graph execution repeatedly crashed due to invalid JPEG encodings in Microsoft PetImages dataset. I wrote an automated sanitization script that pre-scanned the directory headers, leading to the identification and removal of **499 corrupt images**. This stabilized the training pipeline completely.

### 2. Model Evaluation & Overfitting Analysis
Epoch 10.10 -> Training Accuracy: 97,77% | Validation Accuracy: 78,34%

<img width="576" height="455" alt="image" src="https://github.com/user-attachments/assets/10188ca8-c704-4f96-afc4-e390d6cb8213" />

As shown in the evaluation history plots, the model achieves high training performance but experiences a classic divergence in validation accuracy.

**Next Steps for Optimization (WIP):**
* Implement intense **Data Augmentation** (random flips, rotation).
* Integrate **Dropout Layers** before the final dense layers to improve generalization.
* Experimentwith **Transfer Learning** using pre-trained weights like MobileNetV2 for enhanced feature extraction.

---

## How to Run Locally

1. Clone this repository:
  ```
  git clone (https://github.com/brilliannaufal123/pet-prediction-cnn.git)
  ```
2. Install dependencies:
  ```
  pip install tensorflow gradio numpy pillow
  ```
3. Run the application:
  ```
  python app.py
  ```
