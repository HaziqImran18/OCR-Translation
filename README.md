
# 📄 OCR Translator App

A lightweight and efficient web app to extract text from images using Tesseract OCR and translate it into multiple languages using Googletrans — all powered by an interactive Streamlit interface.

---

## 📦 Setup Instructions

### 🔹 Create and activate virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 🔹 Install dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Install Tesseract OCR Engine
Download and install from the following link:  
👉 [Tesseract for Windows (UB Mannheim build)](https://github.com/UB-Mannheim/tesseract/wiki)

During installation, note the path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`)

Then, add path in your script (if needed):
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 🚀 Run the App
```bash
streamlit run app.py
```

---

## 🖼️ Screenshots

📌 Add your screenshots here using the format below:
```scss
![Upload Image](screenshots/upload.png)
![Extracted & Translated Text](screenshots/translated.png)
```

---

## 🌐 Supported Languages

You can extend or change translation languages easily. Current supported examples:

- 🇺🇾 Urdu  
- 🇫🇷 French  
- 🇩🇪 German  
- 🇪🇸 Spanish  
- 🇮🇳 Hindi  

---

## 📁 File Structure

```bash
ocr-translator-app/
│
├── app.py               # Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # Project overview and usage
└── screenshots/         # Add screenshots of app usage
```

---

## 🤝 Credits

- OCR: Tesseract OCR  
- Translation: Googletrans  
- UI: Streamlit  
