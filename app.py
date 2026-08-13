import streamlit as st
import joblib
import re

model = joblib.load('phishing_model.pkl')

st.title('Phishing & Malicious URL Detector')
url_input = st.text_input('Enter a URL to scan:')