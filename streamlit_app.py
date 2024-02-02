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
st.header("Hepatitis Prediction")
st.subheader('User Input:')
st.write(user_input)

prediction = loaded_model.predict(user_input)

st.subheader('Prediction:')
if prediction[0]==1:
    st.write('The patient is hepatitis positive')
else:
    st.write('The patient is hepatitis negative')

st.subheader("Attributes Description")
st.text("Age: The patient's chronological age.")
st.text("Sex: The patient's gender(0 - Male & 1 - Female).")
st.text("Steroid: The presence of steroid hormones in the blood.")
st.text("Antivirals: The use of antiviral medications.")
st.text("Fatigue: Excessive tiredness that interferes with daily activities.")
st.text("Malaise: General feeling of discomfort, such as a sense of uneasiness or ill-being.")
st.text("Anorexia: Loss of appetite or decrease in food intake.")
st.text("Liver Big: Enlargement of the liver.")
st.text("Liver Firm: The liver feels firm during physical examination.")
st.text("Spleen Palpable: The spleen is felt through physical examination.")
st.text("Spiders: Small red spots on the skin.")
st.text("Ascites: Accumulation of fluid in the abdomen, causing swelling.")
st.text("Varices: Dilated veins near the surface of the skin.")
st.text("Bilirubin: A yellow pigment produced during the breakdown of red blood cells.")
st.text("Alk Phosphate: A waste product produced by the body.")
st.text("SGOT: Alanine aminotransferase, an enzyme found in the liver.")
st.text("Albumin: A protein made by the liver and other tissues.")
st.text("Protime: A blood clotting factor.")
st.text("Histology: The study of the microscopic structure of tissues(0 - Normal & 1 - Abnormal).")
