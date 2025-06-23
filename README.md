# 🌿 Plant Disease Detection Using Deep Learning

This project implements a **plant disease detection system** using deep learning and Flask. The application identifies diseases in plant leaves and suggests appropriate remedies by querying a **Firebase Realtime Database**.

---

## 🚀 Features

- 🧠 Trained deep learning model (ResNet34 via FastAI)
- 🌱 Detects diseases in crops: Tomato, Potato, Grape, Apple
- 🔥 Dynamic remedy retrieval from Firebase Realtime Database
- ⚡ Flask-based backend for predictions and remedy display
- 📦 Docker-ready setup for deployment
- ☁️ Google Cloud (or any server) compatible

---

## 🧠 Technologies Used

- **Python, FastAI, Flask**
- **Firebase Realtime Database**
- **Docker (For deployment)**
- **HTML/CSS + JS** 

---


---

## 🧪 Model Details

- **Architecture:** ResNet34
- **Framework:** FastAI
- **Dataset:** PlantVillage
- **Accuracy:** ~98% on validation set

---

## 🔌 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/spacedragonx/PDD.git
cd plant-disease-detection
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Set Up Firebase

- Create a Firebase Realtime Database

- Import plant_diseases.json into the database

- Add your Firebase credentials to firebase_util.py

### 4. Run the Flask App

```bash
cd app
python server.py serve
```


### 5. 📦 Docker (Optional)
Build the Flask app container:
```bash
docker build -t plant-flask-app .
docker run -p 5000:5000 plant-flask-app
```

## 🧾 Firebase DB Format
```
{
  "Tomato___Early_blight": {
    "overview": "Fungal disease caused by Alternaria...",
    "remedy": "Use crop rotation and apply appropriate fungicides."
  },
  ...
}
```


## ✨ Future Enhancements
- Add user image history or tracking

- Integrate live webcam support

- Expand to more plant types and diseases

- Add confidence scores to predictions