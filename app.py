

import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image



pickle_in = open("model.pkl","rb")
model =pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_readmission(input_df):
    """Make prediction based on user inputs in DataFrame format"""
    prediction = model.predict(input_df)
    return prediction[0]


def get_user_input():
    """Gather user input via Streamlit and return a DataFrame for prediction"""
    age = st.text_input("Age")
    length_of_stay = st.text_input("Length of Stay (in days)")
    gender = st.selectbox("Gender", options=["Male", "Female"])
    
    
    # Convert gender input to numeric
    gender = 1 if gender == "Male" else 0

    # Convert inputs to a dictionary and then DataFrame
    input_data = {
        'age': [age],
        'gender': [gender],
        'length_of_stay': [length_of_stay]
        
    }

    input_df = pd.DataFrame(input_data)
    
    return input_df


def main():
    st.title("RedefineCare")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Failure Readmission Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    input_df = get_user_input()
    result=""
    if st.button("Predict"):
        result = predict_readmission(input_df)
        st.success('Readmission within 30 days' if result == 1 else 'No readmission within 30 days')
   
if __name__=='__main__':
    main()
    
    
    