# Image Caption Generator

This is a **Streamlit web application** that generates descriptive captions for uploaded images using a **pre-trained BLIP (Bootstrapped Language-Image Pretraining)** model from Hugging Face's Transformers library.

---

Try out the application via following [Link](https://tobiaskothbauer-image-captioning-image-caption-webapp-qfxfbr.streamlit.app/)

---

## Features

- **Upload an Image**: Upload an image file (JPG, JPEG, or PNG) from your computer.
- **Generate Caption**: Automatically generates a textual description for the uploaded image.
- **Display Result**: Displays the uploaded image along with its generated caption.

---

## Requirements

To run this application, you need the following dependencies:

- **Python 3.10+**
- **Streamlit**
- **Transformers**
- **Torch**
- **Pillow**

---

## How It Works

- **Model**:  
  The app uses the `Salesforce/blip-image-captioning-base` model from Hugging Face.

- **Upload**:  
  Upload any image file.

- **Processing**:  
  - The BLIP processor prepares the image for the model.  
  - The model generates a caption based on the image content.

- **Output**:  
  The app displays the uploaded image and the generated caption.

---

## How to Run the Application locally

### Clone this repository:

```bash
git clone https://github.com/yourusername/image-caption-generator.git
cd image-caption-generator
```
### Install Dependencies

Install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```

### Run the application using Streamlit:
```bash
streamlit run image_caption_webapp.py
```

