import streamlit as st
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    BlipForQuestionAnswering
)
from PIL import Image
import torch

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Multimodal AI App",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Multimodal AI App")
st.write("Image Captioning + Visual Question Answering")

# -----------------------------
# LOAD MODELS
# -----------------------------

@st.cache_resource
def load_caption_model():
    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    return processor, model


@st.cache_resource
def load_vqa_model():
    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-vqa-base"
    )

    model = BlipForQuestionAnswering.from_pretrained(
        "Salesforce/blip-vqa-base"
    )

    return processor, model


caption_processor, caption_model = load_caption_model()
vqa_processor, vqa_model = load_vqa_model()

# -----------------------------
# IMAGE UPLOAD
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    # -----------------------------
    # IMAGE CAPTIONING
    # -----------------------------

    st.subheader("🖼 Image Caption")

    if st.button("Generate Caption"):

        inputs = caption_processor(
            image,
            return_tensors="pt"
        )

        output = caption_model.generate(
            **inputs,
            max_new_tokens=20
        )

        caption = caption_processor.decode(
            output[0],
            skip_special_tokens=True
        )

        st.success(caption)

    # -----------------------------
    # VISUAL QUESTION ANSWERING
    # -----------------------------

    st.subheader("❓ Ask Question About Image")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Get Answer"):

        if question.strip() != "":

            inputs = vqa_processor(
                image,
                question,
                return_tensors="pt"
            )

            output = vqa_model.generate(
                **inputs,
                max_new_tokens=10
            )

            answer = vqa_processor.decode(
                output[0],
                skip_special_tokens=True
            )

            st.success(answer)

        else:
            st.warning("Please enter a question.")