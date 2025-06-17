import streamlit as st
import pandas as pd
import random
import os

# -------------- Topics List ------------------
topics = [
    "Python Basics", "Data Types", "Variables", "Loops", "Functions", "File Handling",
    "Pandas", "Numpy", "Matplotlib", "Seaborn", "Data Cleaning",
    "Statistics", "EDA", "Regression", "Classification", "Clustering",
    "Model Evaluation", "Feature Engineering", "Deep Learning Intro"
]

practice_questions = {
    "Python Basics": [
        "Explain the difference between list and tuple.",
        "Write a Python program to reverse a string.",
        "Explain indentation importance in Python."
    ],
    "Variables": [
        "What is dynamic typing?",
        "Give examples of variable naming rules.",
        "How does Python manage memory allocation?"
    ],
    "Functions": [
        "Explain default arguments with example.",
        "What are lambda functions?",
        "Write a function to calculate factorial."
    ],
    "Pandas": [
        "How to handle missing values in pandas?",
        "Explain difference between loc[] and iloc[].",
        "Write code to merge two DataFrames."
    ],
    "Numpy": [
        "How to create a numpy array with random values?",
        "What is broadcasting in numpy?",
        "Difference between numpy array and list."
    ],
    "EDA": [
        "Explain correlation and covaria
