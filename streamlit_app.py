import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.title("Student Exam Performance Predictor")

# Input fields
gender = st.selectbox("Gender", ["male", "female"])
ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_education = st.selectbox("Parental Level of Education", [
    "associate's degree", "bachelor's degree", "high school",
    "master's degree", "some college", "some high school"])
lunch = st.selectbox("Lunch Type", ["free/reduced", "standard"])
prep_course = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.number_input("Reading Score", min_value=0, max_value=100)
writing_score = st.number_input("Writing Score", min_value=0, max_value=100)

# Predict button
if st.button("Predict Math Score"):
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_education,
        lunch=lunch,
        test_preparation_course=prep_course,
        reading_score=reading_score,
        writing_score=writing_score
    )
    input_df = data.get_data_as_data_frame()
    predictor = PredictPipeline()
    prediction = predictor.predict(input_df)
    st.success(f"Predicted Math Score: {prediction[0]:.2f}")