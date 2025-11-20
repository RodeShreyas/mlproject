# Student Exam Performance Predictor End to End Machine Learning Project

## Introduction
➢ The Student Exam Performance Prediction project is an end-to-end Machine Learning system designed to predict a student’s exam score based on various academic, demographic, and personal factors. The goal of this project is to demonstrate a complete ML lifecycle—from data ingestion and preprocessing to model training, evaluation, and deployment.

➢ This project follows a production-ready architecture with modular code, exception handling, logging, reusable utilities, and CI/CD-friendly structure. The final model is deployed as an interactive Streamlit web application, allowing users to input student details and instantly receive a predicted performance score.

➢ This project showcases industry-standard ML project structure and is suitable for resumes, interviews, and demonstrating real-world ML engineering skills.

## Aim
To build and deploy an end-to-end machine learning system that predicts a student’s exam performance based on demographic, academic, and environmental features, enabling data-driven insights for educators, parents, and learners.

## Objectives
➢ To collect, preprocess, and transform raw student performance data into meaningful features suitable for ML modeling.

➢ To design a modular machine learning pipeline consisting of data ingestion, validation, transformation, model training, evaluation, and prediction components.

➢ To experiment with multiple ML algorithms and identify the best-performing model for predicting exam scores.

➢ To implement exception handling, logging, custom utilities, and a scalable project structure following industry best practices.

➢ To save trained models, preprocessing pipelines, and metadata using serialization techniques (pickle/joblib).

➢ To deploy the prediction pipeline using Streamlit, providing a user-friendly web interface for real-time exam score prediction.

## Methodology
The project follows a complete End-to-End Machine Learning Pipeline, ensuring that the system is production-ready and scalable. The major steps involved are:

1️. Data Ingestion
Load the Student Exam Performance dataset from CSV.
Perform basic checks (null values, schema).
Split the data into training and testing sets.
Save processed datasets into the artifact folder for reproducibility.

2️. Data Transformation
Handle missing values.
Convert categorical variables into numerical using:
One-Hot Encoding
Label Encoding 
Apply feature scaling using StandardScaler.
Combine transformed features into a final NumPy array.
Save preprocessor object (preprocessor.pkl) for use during prediction.

3️. Model Training
Train multiple regression models such as:
Linear Regression
Random Forest Regressor
Gradient Boosting Regressor
XGBoost 

Evaluate models using metrics:
R² Score
MAE (Mean Absolute Error)
RMSE (Root Mean Square Error)
Select the best model based on performance.
Save the trained model (model.pkl) for deployment.

4️. Prediction Pipeline
Accept user input from Streamlit UI.
Convert inputs into a DataFrame.
Apply saved preprocessing object.
Pass transformed features to the trained model.
Return the predicted exam score on UI.

5️. Exception Handling & Logging
Implement a custom exception class (CustomException) for:
Error traceability
Debugging complex failures
Maintain detailed application logs using logging.py
Pipeline steps
Errors & Warnings
Model saving stages

6️. Deployment
Streamlit Cloud Deployment
Build a clean UI using Streamlit.
Upload the project to GitHub.
Deploy directly using Streamlit Cloud.
Public URL generated for demo access.
Access the deployed application here: https://rodeshreyas-mlproject-streamlit-app-ewozjo.streamlit.app/

## Tech Stack Used
Languages & Libraries:
Python
NumPy
Pandas
Matplotlib / Seaborn
Scikit-learn
Streamlit
Pickle

ML Algorithms:
Linear Regression
Ridge / Lasso
Random Forest
XGBoost / CatBoost 

Deployment Tools:
Streamlit Cloud

## Output
The model predicts the final math exam score of a student.
