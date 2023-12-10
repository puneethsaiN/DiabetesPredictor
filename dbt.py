import numpy as np
import pickle
import pandas as pd
import streamlit as st

import warnings
warnings.filterwarnings('ignore')

pickle_in = open("classifier.pkl", 'rb')
clf = pickle.load(pickle_in)

st.title('Diabetes Predictor')

html_temp = """
    <div style="background-color:red;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Diabetes Risk Predictor ML App </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

age = 30
g = st.radio("Gender", ['Male', 'Female', 'Other'], index=2)
age = st.text_input("age")
radio1 = st.radio("are you diagnosed with hypertension?", ['Yes', 'No'], key='r1', index=1)
radio2 = st.radio("are you diagnosed with any heart-disease?", ['Yes', 'No'], key='r2', index=1)
box1 = st.selectbox('Smoking History', ['No Info', 'never', 'former', 'current', 'not current', 'ever'])
bmi = st.text_input("BMI [Range 0 to 50]")
hba1c = st.text_input("HbA1c_level [Range 1 to 8]")
bgl = st.text_input("blood_glucose_level [Range 90 to 150]")

#convert string data to numbers for prediction
gender = 0
if g == 'Male':
    gender = 0
elif g == 'Female':
    gender = 1
else:
    gender = 2
    
hpt = 0
if radio1 == 'Yes':
    hpt = 1

hd = 0
if radio2 == 'Yes':
    hd = 1

sh = 0
if box1 == 'No Info':
    sh = 0
elif box1 == 'never':
    sh = 1
elif box1 == 'former':
    sh = 2
elif box1 == 'current':
    sh = 3
elif box1 == 'not current':
    sh = 4
elif box1 == 'ever':
    sh = 5

print(gender, age, hpt, hd, sh, bmi, hba1c, bgl)
result=""
if st.button("Predict"):
    result=clf.predict([[gender, age, hpt, hd, sh, bmi, hba1c, bgl]])
    if(result[0]==0):
        st.success('Congractulations! You are not at risk of Diabetes')
    else:
        st.success('You are at risk of Diabetes')

if st.button("About"):
    st.text("Made by Puneeth")
    st.text("Built with Sklearn RFC and Streamlit")
