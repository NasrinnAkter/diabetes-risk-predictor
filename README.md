# Diabetes Risk Predictor

A machine learning project that predicts diabetes risk from health measurements, with a web app to try it.

Live demo: https://diabetes-risk-predictor-nasrin.streamlit.app/

## About
I used the Pima Indians Diabetes dataset (768 patients, 8 measurements like glucose, BMI and age). I cleaned the data, compared three models, and deployed the best one with Streamlit.

## What I did
- Some columns (Glucose, Insulin, BMI, etc.) had 0 where the value was actually missing, so I replaced those with the median.
- Compared Logistic Regression, Random Forest and Gradient Boosting.
- Picked Gradient Boosting: about 76% test accuracy, F1 of 0.63.
- Built the app with Streamlit.

## Notes
The dataset is small, so the accuracy isn't very high. This is a learning project, not for medical use.

Built with Python, pandas, scikit-learn and Streamlit.
