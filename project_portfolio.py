import streamlit as st
import pandas as pd
import os

# File for portfolio data
PORTFOLIO_FILE = "portfolio.csv"

# Create file if not exist
if not os.path.exists(PORTFOLIO_FILE):
    df = pd.DataFrame(columns=["Project Name", "Description", "Skills Used", "Project Link", "Status"])
    df.to_csv(PORTFOLIO_FILE, index=False)

# Load existing data
df = pd.read_csv(PORTFOLIO_FILE)

# Streamlit UI
st.title("📂 Personal Project Portfolio Manager")

# Form to add project
with st.form("add_project"):
    project_name = st.text_input("Project Name")
    description = st.text_area("Project Description")
    skills = st.text_input("Skills Used (comma separated)")
    project_link = st.text_input("Project Link (GitHub / Kaggle / Other)")
    status = st.selectbox("Project Status", ["In Progress", "Completed", "Planned"])
    submit = st.form_submit_button("Save Project")

    if submit:
        new_row = {
            "Project Name": project_name,
            "Description": description,
            "Skills Used": skills,
            "Project Link": project_link,
            "Status": status
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(PORTFOLIO_FILE, index=False)
        st.success("✅ Project Saved")

# Display all projects
st.subheader("📊 Current Portfolio")
st.dataframe(df)
