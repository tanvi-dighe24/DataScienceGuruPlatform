import streamlit as st
import random
import pandas as pd
import os
from datetime import datetime

# Simple interview question bank
question_bank = [
    "Explain the difference between supervised and unsupervised learning.",
    "What is overfitting? How to avoid it?",
    "What is the bias-variance tradeoff?",
    "How does a decision tree work?",
    "Explain PCA (Principal Component Analysis).",
    "What is gradient descent?",
    "How do you handle missing data?",
    "What is the difference between classification and regression?",
    "Explain the role of activation functions in neural networks.",
    "How does cross-validation work?",
    "What is regularization in machine learning?",
    "How would you deal with imbalanced datasets?",
    "What is feature engineering?",
    "Explain confusion matrix and related metrics.",
    "How do recommendation systems work?"
]

# File to save answers
ANSWER_FILE = "interview_answers.csv"

if not os.path.exists(ANSWER_FILE):
    df = pd.DataFrame(columns=["Date", "Question", "Answer"])
    df.to_csv(ANSWER_FILE, index=False)

st.title("🎙️ AI Interview Preparation")

# Generate Random Question
if st.button("Generate Question"):
    question = random.choice(question_bank)
    st.session_state.question = question

# If question generated, show form
if "question" in st.session_state:
    st.subheader("Today's Question:")
    st.write(st.session_state.question)

    answer = st.text_area("Your Answer:")

    if st.button("Save Answer"):
        df = pd.read_csv(ANSWER_FILE)
        new_row = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Question": st.session_state.question,
            "Answer": answer
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(ANSWER_FILE, index=False)
        st.success("✅ Your answer is saved!")

# Show past answers
if st.checkbox("Show My Previous Answers"):
    df = pd.read_csv(ANSWER_FILE)
    st.dataframe(df)
