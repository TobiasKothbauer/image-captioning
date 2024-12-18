import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch


# Load the BLIP model and processor
@st.cache_resource()
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model


def generate_caption(image, processor, model):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption


def main():
    # Load the model and processor
    processor, model = load_model()

    st.title("Image Caption Generator")
    st.write("Upload an image, and the app will generate a description for it.")

    # Image uploader
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open and display the image
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Generate caption
        with st.spinner('Generating caption...'):
            caption = generate_caption(image, processor, model)

        # Display the caption
        st.success("Generated Caption:")
        st.write(f"**{caption}**")


if __name__ == "__main__":
    main()
