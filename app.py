import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator
import os

# Configure tesseract path if needed (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Streamlit UI setup
st.set_page_config(page_title="Image OCR + Translator", layout="centered")
st.title("🌐 OCR + Text Translator")
st.markdown("Upload an image with text and translate the extracted text into your chosen language.")

# Sidebar for upload and language selection
st.sidebar.header("📤 Upload & Settings")
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
target_lang = st.sidebar.selectbox("Translate to Language", options=["en", "ur", "fr", "es", "de", "zh-cn"], index=1)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image)
        st.subheader("📝 Extracted Text")
        st.text_area("", value=extracted_text, height=150)

        translator = Translator()
        translated = translator.translate(extracted_text, dest=target_lang)

        st.subheader(f"🌍 Translated Text ({target_lang.upper()})")
        st.text_area("", value=translated.text, height=150)

        # Optional download
        st.download_button("💾 Download Translated Text", translated.text, file_name="translated_text.txt")
