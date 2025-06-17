import streamlit as st
import pandas as pd
import os

# File to store job applications
JOBS_FILE = "job_applications.csv"

# Create file if doesn't exist
if not os.path.exists(JOBS_FILE):
    df = pd.DataFrame(columns=["Company", "Position", "Applied Date", "Status", "Notes"])
    df.to_csv(JOBS_FILE, index=False)

# Load file
df = pd.read_csv(JOBS_FILE)

# Streamlit App
st.title("💼 Job & Internship Tracker")

# Form to add new job application
with st.form("add_job"):
    company = st.text_input("Company Name")
    position = st.text_input("Position Title")
    applied_date = st.date_input("Applied Date")
    status = st.selectbox("Application Status", ["Applied", "Interview Scheduled", "Offer Received", "Rejected", "No Response"])
    notes = st.text_area("Notes")

    submitted = st.form_submit_button("Save Application")

    if submitted:
        new_row = {
            "Company": company,
            "Position": position,
            "Applied Date": applied_date,
            "Status": status,
            "Notes": notes
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(JOBS_FILE, index=False)
        st.success("✅ Application Saved")

# Display current applications
st.subheader("📋 Current Applications")
st.dataframe(df)
