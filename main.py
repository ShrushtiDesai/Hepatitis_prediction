import streamlit as st
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import pickle
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def get_user_input():
    age = st.sidebar.slider('Age', 5, 80, 30)
    sex = st.sidebar.slider('Sex', 0, 1, 0)
    steroid = st.sidebar.slider('Steroid', 0, 2, 1)
    antivirals = st.sidebar.slider('Antivirals', 0, 1, 0)
    fatigue = st.sidebar.slider('Fatigue', 0, 2, 1)
    malaise = st.sidebar.slider('Malaise', 0, 2, 1)
    anorexia = st.sidebar.slider('Anorexia', 0, 2, 1)
    liver_big = st.sidebar.slider('Liver Big', 0, 2, 1)
    liver_firm = st.sidebar.slider('Liver Firm', 0, 2, 1)
    spleen_palpable = st.sidebar.slider('Spleen Palpable', 0, 2, 1)
    spiders = st.sidebar.slider('Spiders', 0, 2, 1)
    ascites = st.sidebar.slider('Ascites', 0, 2, 1)
    varices = st.sidebar.slider('Varices', 0, 2, 1)
    bilirubin = st.sidebar.slider('Bilirubin', 0.0, 10.0, 0.8)
    alk_phosphate = st.sidebar.slider('Alk Phosphate', 10.0, 300.0, 30.0)
    sgot = st.sidebar.slider('SGOT', 0.0, 1000.0, 30.0)
    albumin = st.sidebar.slider('Albumin', 0.0, 1000.0, 30.0)
    protime = st.sidebar.slider('Protime', 0.0, 100.0, 30.0)
    histology = st.sidebar.slider('Histology', 0, 1, 1)
    user_data = { 'age': age,
                  'sex': sex,
                  'steroid': steroid,
                  'antivirals': antivirals,
                  'fatigue': fatigue,
                  'malaise': malaise,
                  'anorexia': anorexia,
                  'liver_big': liver_big,
                  'liver_firm': liver_firm,
                  'spleen_palpable': spleen_palpable,
                  'spiders': spiders,
                  'ascites': ascites,
                  'varices': varices,
                  'bilirubin': bilirubin,
                  'alk_phosphate': alk_phosphate,
                  'sgot': sgot,
                  'albumin': albumin,
                  'protime': protime,
                  'histology': histology }

    features = pd.DataFrame(user_data, index=[0])
    return features

user_input = get_user_input()

st.subheader('User Input:')
st.write(user_input)

prediction = loaded_model.predict(user_input)

st.subheader('Prediction:')
if prediction[0]==1:
    st.write('The patient is hepatitis positive')
else:
    st.write('The patient is hepatitis negative')

st.title("Attributes Description")
st.text("For the Age attribute  0 represents Male and 1 represents Female")
