# 📌 LSB Steganography Tool Documentation

## 📖 Overview
This **LSB Steganography Tool** allows you to hide and extract secret messages inside image files using **Least Significant Bit (LSB) encoding**. It provides a command-line interface (CLI) for ease of use.

## 🚀 Features
✅ Embed secret messages into images using LSB encoding  
✅ Extract hidden messages from encoded images  
✅ Supports PNG and BMP image formats  
✅ CLI with progress bars and colored outputs for better UX  

---
## 📥 Installation
Ensure you have **Python 3.8+** installed.

Install dependencies:
```bash
pip install pillow numpy tqdm colorama
```

---
## 🔧 Usage
Run the tool using the command line.

### 🖼️ **Embedding a Message**
```bash
python main.py encode <image_path> --message "Your secret message" --output <output_image>
```
📌 **Example:**
```bash
python main.py encode input.png --message "Hello, World!" --output output.png
```
✅ This will create `output.png` with the hidden message.

### 🎭 **Extracting a Message**
```bash
python main.py decode <image_path>
```
📌 **Example:**
```bash
python main.py decode output.png
```
✅ This will print the extracted hidden message.

---
## 📜 Modules Breakdown
### **1️⃣ ImageProcessor (image_processor.py)**
- Loads and saves images
- Converts images into pixel matrices

### **2️⃣ Encoder (encoder.py)**
- Embeds a secret message into an image

### **3️⃣ Decoder (decoder.py)**
- Extracts a hidden message from an encoded image

### **4️⃣ CLI Interface (main.py)**
- Provides a user-friendly command-line interface
- Displays progress bars and colored output

---
## 🎨 CLI Enhancements
🔍 **Progress bar** for embedding/extraction using `tqdm`  
✅ **Colored output** using `colorama`  
📢 **Interactive prompts** for better usability  

---
## ❗ Limitations
- Only works with **PNG/BMP** images (JPEG not supported due to compression).
- Large messages might not fit in small images.

---
## 🤝 Contributing
Feel free to contribute! Fork the repository and submit a **pull request**.

---
## 📜 License
This project is **open-source** under the MIT License.

---
🚀 **Happy Steganography!** 🎭

