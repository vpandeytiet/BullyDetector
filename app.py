# Code for getting toxic_comments.db from releases

import streamlit as st
import requests
import os
import sqlite3

# Function to download large files if they don't exist
def download_file(url, filename):
    if not os.path.exists(filename):
        st.info(f"Downloading {filename}...")
        response = requests.get(url, stream=True)
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        st.success(f"{filename} downloaded successfully!")

# GitHub Release URL (Replace with actual URL)
DB_URL = "https://github.com/vpandeytiet/BullyDetector/releases/download/v1.0/toxic_comments.db"

# Download database if missing
download_file(DB_URL, "toxic_comments.db")

# Connect to SQLite database
conn = sqlite3.connect("toxic_comments.db")
cursor = conn.cursor()

# Example Query: Fetch data
#cursor.execute("SELECT * FROM comments LIMIT 5")
#data = cursor.fetchall()
#st.write("Sample Data:", data)

# Code for getting 2 datasets train.csv and test.csv from releases

import streamlit as st
import requests
import os
import pandas as pd

# Function to download large files if they don't exist
def download_file(url, filename):
    if not os.path.exists(filename):
        st.info(f"Downloading {filename}...")
        response = requests.get(url, stream=True)
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        st.success(f"{filename} downloaded successfully!")

# GitHub Release URLs (Replace with your actual URLs)
TRAIN_CSV_URL = "https://github.com/vpandeytiet/BullyDetector/releases/download/v2.0/train.csv"
TEST_CSV_URL = "https://github.com/vpandeytiet/BullyDetector/releases/download/v2.0/test.csv"

# Download CSVs if missing
download_file(TRAIN_CSV_URL, "train.csv")
download_file(TEST_CSV_URL, "test.csv")

# Load Data
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# Display Sample Data
#st.write("Sample Train Data:", train_df.head())
#st.write("Sample Test Data:", test_df.head())





#Main Code

import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load trained models
vec = pickle.load(open("tfidf_vectorizer.pkl", "rb"))
toxic_classifier = pickle.load(open("toxic_classifier.pkl", "rb"))
models = pickle.load(open("toxic_models.pkl", "rb"))

st.title("🔹 AI-Powered Toxic Comment Classifier")
st.write("This model first checks if a comment is **Toxic** or **Non-Toxic**. If it's Toxic, it categorizes it into specific types.")

user_input = st.text_area("Enter a comment:")
if st.button("Analyze Comment"):
    if user_input:
        comment_vec = vec.transform([user_input])
        is_toxic = toxic_classifier.predict(comment_vec)[0]
        if is_toxic == 0:
            st.success("✅ This comment is **Non-Toxic**!")
        else:
            st.warning("⚠️ This comment is **Toxic**! Categorizing further...")
            predictions = {label: models[label].predict_proba(comment_vec)[:,1][0] for label in models}
            st.write("\n### 🔹 Toxicity Predictions:")
            for category, score in predictions.items():
                st.write(f"**{category}:** {round(score * 100, 2)}%")
            most_likely_category = max(predictions, key=predictions.get)
            st.write("\n### 🔹 Most Likely Toxic Category:", most_likely_category)
    else:
        st.warning("Please enter a comment first.")
