# Facial Expression Recognition using Deep Learning

This project focuses on building and comparing two deep learning models for facial expression recognition using computer vision techniques. 
The system detects faces in real-time using the Haar Cascade frontal face classifier and classifies emotions into seven categories.

## 📌 Project Overview

Developing and evaluating two models:
- 🧠 Custom CNN (built from scratch using Keras)
- 🚀 Transfer Learning model based on MobileNetV2 (fine-tuned)

Both models are deployed in a Streamlit web app to perform real-time emotion detection using a webcam, allowing side-by-side comparison.


## 📂 Dataset
- Source: Kaggle – Face Expression Recognition Dataset
- Classes (7 emotions): Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise


## 🧠 Models

### 1. Custom CNN Model
- Built from scratch using Keras
- Trained on grayscale facial images
- Architecture includes:
- Convolutional layers
- MaxPooling layers
- Fully connected layers
- Dropout for regularization

#### 📊 Performance
- Accuracy score: 66%
- Key Observations:
- Happy: 85% accuracy score (best predicted)
- Fear: 39% accuracy score (worst predicted)


### 2. MobileNetV2 (Transfer Learning)
- Pretrained MobileNetV2 model
- Fine-tuned on the dataset
- Uses transfer learning to leverage pretrained features

#### 📊 Performance
- Accuracy score: 61%
- Key Observations:
- Happy: 76% accuracy score (best predicted)
- Fear: 47% accuracy score (worst predicted)


## ⚖️ Model Comparison
- The CNN model achieves higher overall accuracy score.
- The MobileNetV2 model provides more consistent predictions across classes.


## 📊 Evaluation
- Confusion Matrix used for detailed performance analysis
- Strong performance on Happy
- Difficulty distinguishing Fear from similar expressions


## 🎥 Real-Time Application

A Streamlit app is implemented to:
- Capture video from the webcam
- Detect faces using Haar Cascade
- Run both models simultaneously
- Display predictions side-by-side in real time

### Features
- 🔍 Face detection using Haar Cascade
- 🎭 Emotion prediction overlay
- ⚡ Parallel inference (CNN vs MobileNetV2)
- 📺 Live comparison interface


## 🛠️ Tech Stack
- Python
- TensorFlow / Keras
- OpenCV
- Streamlit
- NumPy / Pandas / Matplotlib
