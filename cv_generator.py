import streamlit as st
import pandas as pd
import os

# Load portfolio data
PORTFOLIO_FILE = "portfolio.csv"

if os.path.exists(PORTFOLIO_FILE):
    portfolio_df = pd.read_csv(PORTFOLIO_FILE)
else:
    portfolio_df = pd.DataFrame(columns=["Project Name", "Description", "Skills Used", "Project Link", "Status"])

st.title("📄 Auto CV Generator")

# Basic Info Form
with st.form("cv_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn Profile")
    github = st.text_input("GitHub Profile")
    skills = st.text_area("List your key skills (comma separated)")

    submitted = st.form_submit_button("Generate CV")

if submitted:
    st.subheader("✅ Your Auto Generated CV:")

    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    st.write(f"**LinkedIn:** {linkedin}")
    st.write(f"**GitHub:** {github}")

    st.write("**Skills:**")
    for skill in skills.split(","):
        st.write(f"- {skill.strip()}")

    st.write("**Projects:**")
    for i, row in portfolio_df.iterrows():
        st.write(f"- **{row['Project Name']}**: {row['Description']} (Skills: {row['Skills Used']}) [Link]({row['Project Link']})")

    st.success("🎯 You can copy this text into MS Word/Google Docs for your resume.")
