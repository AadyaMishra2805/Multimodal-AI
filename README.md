# Multimodal-AI
Multimodal AI App 🤖

A multimodal AI application built using Streamlit, Hugging Face Transformers, and BLIP models.

This project combines:

Image Caption Generation
Visual Question Answering (VQA)

The application allows users to upload an image, generate captions, and ask questions about the image using AI.

Features
Image Caption Generator

Upload an image and automatically generate an AI-based caption.

Example:
Input Image → Dog Image
Output → A black dog standing on grass

Visual Question Answering (VQA)

Ask questions related to the uploaded image.

Example:
Question → What animal is this?
Answer → dog

Tech Stack
Component	Technology
Language	Python
Frontend	Streamlit
Deep Learning	PyTorch
Models	BLIP
Libraries	Transformers, Pillow
Models Used
Captioning Model

Salesforce/blip-image-captioning-base

VQA Model

Salesforce/blip-vqa-base

Project Structure

IMAGE_CAPTION_PROJECT/

├── app1.py
├── README.md
├── requirements.txt
├── sample.png
├── .gitignore

Installation
Clone Repository

git clone https://github.com/AadyaMishra2805/Multimodal-AI.git

Navigate to Project Folder

cd Multimodal-AI

Create Virtual Environment

python -m venv venv

Activate Virtual Environment
Git Bash

source venv/Scripts/activate

CMD

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run Application

streamlit run app1.py

Application Workflow
Image Captioning

Image
↓
BLIP Processor
↓
Vision Encoder
↓
Language Decoder
↓
Generated Caption

Visual Question Answering

Image + Question
↓
BLIP VQA Model
↓
Multimodal Understanding
↓
Generated Answer

Example Outputs
Caption Generation

Generated Caption:
A dog standing on the grass

Visual Question Answering

Question:
What animal is this?

Answer:
dog

Challenges Faced
Dependency conflicts with TensorFlow and protobuf
GitHub large file issues due to virtual environment tracking
Hugging Face model cache handling
Streamlit execution warnings
AI hallucination outputs
Learning Outcomes

This project helped in understanding:

Multimodal AI systems
Vision-language models
Hugging Face Transformers
Streamlit frontend development
Image preprocessing
Text generation
PyTorch inference pipeline
Git and GitHub workflows
Future Improvements
Webcam support
Speech output
Better captioning models
OCR integration
Multiple image support
Cloud deployment
Author

Aadya Mishra

License

This project is for educational and learning purposes.
