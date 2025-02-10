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
