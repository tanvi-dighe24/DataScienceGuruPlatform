import streamlit as st
import pandas as pd
import os
import random
from datetime import datetime, timedelta

# Load progress file
PROGRESS_FILE = "progress.csv"

if not os.path.exists(PROGRESS_FILE):
    st.warning("No progress data found!")
else:
    df = pd.read_csv(PROGRESS_FILE)
    st.title("📅 Auto Revision Planner")

    if df.empty:
        st.info("No progress data available.")
    else:
        # Logic: If score <= 7 → Needs revision
        weak_df = df[df["Score"] <= 7]
        all_topics = df["Topic"].unique()

        # Create Revision Schedule
        revision_plan = []

        today = datetime.now()

        for i, topic in enumerate(weak_df["Topic"].unique()):
            revision_date = today + timedelta(days=i)
            revision_plan.append({"Date": revision_date.strftime("%Y-%m-%d"), "Topic": topic, "Type": "Weak Area"})

        # Also randomly revise strong topics after weak topics done
        remaining_topics = list(set(all_topics) - set(weak_df["Topic"].unique()))
        for i, topic in enumerate(remaining_topics):
            revision_date = today + timedelta(days=len(weak_df) + i)
            revision_plan.append({"Date": revision_date.strftime("%Y-%m-%d"), "Topic": topic, "Type": "Strong Refresh"})

        revision_df = pd.DataFrame(revision_plan)

        st.subheader("📆 Your Smart Revision Schedule")
        st.dataframe(revision_df)
