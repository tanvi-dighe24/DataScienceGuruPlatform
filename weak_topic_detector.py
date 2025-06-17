import streamlit as st
import pandas as pd
import os

# Load progress
PROGRESS_FILE = "progress.csv"

if not os.path.exists(PROGRESS_FILE):
    st.warning("No progress data found!")
else:
    df = pd.read_csv(PROGRESS_FILE)
    st.title("📉 Weak Topic Detector")

    if df.empty:
        st.info("No data available yet.")
    else:
        # Calculate weak topics based on score <= 7
        weak_df = df[df["Score"] <= 7]

        if weak_df.empty:
            st.success("🎯 No weak topics! You're doing great!")
        else:
            st.warning("⚠ You may need to revise these topics:")
            st.dataframe(weak_df[["Day", "Topic", "Score", "Comments"]])
