
# 📄 OCR Translator App

A lightweight and efficient web app to extract text from images using Tesseract OCR and translate it into multiple languages using Googletrans — all powered by an interactive Streamlit interface.

---

## 🔍 Features

- ✅ Upload images in `.jpg`, `.jpeg`, or `.png` formats  
- ✅ OCR powered by **Tesseract**  
- ✅ Language translation via **Google Translate API**  
- ✅ Translates to Urdu, French, German, and more  
- ✅ Clean sidebar-based UI  
- ✅ Text preview and optional download  

---

## 📦 Setup Instructions

### 🔹 Clone the repository
   ```bash
git clone https://github.com/HaziqImran18/OCR-Translation.git
cd ocr-translator-app
   ```

### 🔹 Create and activate virtual environment (optional but recommended)
```bash
python -m venv translator
translator\Scripts\activate
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
```

---

## 🤝 Credits

- OCR: Tesseract OCR  
- Translation: Googletrans  
- UI: Streamlit  
