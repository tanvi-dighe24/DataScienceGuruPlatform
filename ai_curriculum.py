import streamlit as st
import pandas as pd
import random
import os

# Topics list (initial version)
topics = [
    "Python Basics", "Data Types", "Variables", "Loops", "Functions", "File Handling",
    "Pandas", "Numpy", "Matplotlib", "Seaborn", "Data Cleaning",
    "Statistics", "EDA", "Regression", "Classification", "Clustering",
    "Model Evaluation", "Feature Engineering", "Deep Learning Intro"
]

# Progress file
PROGRESS_FILE = "progress.csv"
if not os.path.exists(PROGRESS_FILE):
    df = pd.DataFrame(columns=["Day", "Topic", "Score", "Comments"])
    df.to_csv(PROGRESS_FILE, index=False)

# Load current progress
df = pd.read_csv(PROGRESS_FILE)

# Header
st.title("🚀 Tanvi's AI Curriculum Planner")

# Suggest random new topic
completed_topics = df["Topic"].tolist()
remaining_topics = list(set(topics) - set(completed_topics))

if remaining_topics:
    suggestion = random.choice(remaining_topics)
    st.success(f"Today's Suggested Topic: **{suggestion}** 🎯")
else:
    st.info("✅ All topics completed! You rock 🤩")

# Form to submit today's progress
with st.form("progress_form"):
    day = st.text_input("Day (e.g. Day 4)")
    topic = st.text_input("Topic Studied")
    score = st.slider("Self Score (out of 10)", 0, 10, 5)
    comments = st.text_area("Comments / Doubts")

    submitted = st.form_submit_button("Save Progress")
    if submitted:
        new_data = {"Day": day, "Topic": topic, "Score": score, "Comments": comments}
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv(PROGRESS_FILE, index=False)
        st.success("✅ Progress Saved Successfully")

# Show current progress
st.header("📊 Current Progress")
st.dataframe(df)
