# BullyDetector

---

# **🚀 AI-Powered Toxic Comment Classifier**  

An **AI-driven application** that detects and categorizes **toxic comments** using **Machine Learning**. The model identifies whether a comment is **toxic or non-toxic** and, if toxic, classifies it into different categories such as **insult, hate speech, threats, and more**.  

---

## **📥 Setup Instructions**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/YOUR_USERNAME/Bully-Detection-Project.git
cd Bully-Detection-Project
```

### **2️⃣ Install Dependencies**  
Ensure Python **3.10** is installed. Then, run:  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Application**  
```bash
streamlit run app.py
```

### **4️⃣ Download Required Files**  
- **Large files** (`.pkl`, `.csv`, `.db`) are **auto-downloaded** when running the app.  
- If files fail to download, manually download them from **GitHub Releases**.

---

## **📌 Assumptions**  
- **Comment Input:** The model assumes user input is a **single comment or short text** for classification.  
- **Pre-Trained Model:** The classifiers were trained on a **balanced dataset** and might require fine-tuning for real-world performance.  
- **Storage & Access:**  
  - Model files (`.pkl`), database (`.db`), and datasets (`.csv`) are stored on **GitHub Releases** for efficient access.  
  - The app dynamically fetches them when deployed.  

---

## **🚀 Live Demo**  
🔗 **[Live App URL](#)** _((https://bullydetector-5panrtybql4bkxuz8ijxdj.streamlit.app/))_
