import streamlit as st
import pandas as pd
import os

# File to store progress
PROGRESS_FILE = "progress.csv"

# If file doesn't exist, create it
if not os.path.exists(PROGRESS_FILE):
    df = pd.DataFrame(columns=["Day", "Topic", "Score", "Comments"])
    df.to_csv(PROGRESS_FILE, index=False)

# Title
st.title("🎯 Tanvi's Data Science Progress Tracker")

# Form to enter today's progress
with st.form("progress_form"):
    day = st.text_input("Day (e.g. Day 3)")
    topic = st.text_input("Topic Studied")
    score = st.slider("Self Score (out of 10)", 0, 10, 5)
    comments = st.text_area("Comments / Doubts")

    submitted = st.form_submit_button("Save Progress")
    if submitted:
        new_data = {"Day": day, "Topic": topic, "Score": score, "Comments": comments}
        df = pd.read_csv(PROGRESS_FILE)
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv(PROGRESS_FILE, index=False)
        st.success("✅ Progress Saved Successfully")

# Display current progress
st.header("📊 Your Current Progress")
df = pd.read_csv(PROGRESS_FILE)
st.dataframe(df)
