# 🩺 Medical Diagnosis Multimodal Chatbot 🤖💬

## 📌 Project Overview

This is a **Multimodal Medical Diagnosis Chatbot** built using Python, NLP, and Computer Vision.  
The chatbot can understand **text symptoms** and **images (like medical reports or prescriptions)** to help analyze and assist in preliminary diagnosis workflows.

This project showcases how AI can be used to build a smart assistant for healthcare applications.

---

## 🧠 Key Features

✅ Accepts text input (symptoms)  
✅ Can process uploaded images (reports/prescriptions)  
✅ NLP-based diagnosis suggestions  
✅ Easy to extend with new models or databases

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| FastAPI | Backend API server |
| HuggingFace Transformers | NLP model for language understanding |
| OpenCV / Tesseract | OCR + image processing |
| Scikit-learn / ML models | Prediction algorithms |
| Streamlit / UI | User interface (if included) |

---

## 📁 Repository Structure

```text
├── app/                      # FastAPI application
├── models/                   # Saved ML/NLP models
├── data/                     # Dataset files
├── utils/                    # Utility functions: preprocess, OCR, etc.
├── requirements.txt
├── main.py                   # Main FastAPI server
└── README.md
