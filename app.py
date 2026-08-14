import streamlit as st
import joblib
import re

model = joblib.load('phishing_model.pkl')

st.title('Phishing & Malicious URL Detector')
url_input = st.text_input('Enter a URL to scan:')

def count_special_chars(url):
    return sum(url.count(c) for c in ['@', '-', '.', '?', '='])

def has_ip(url):
    return 1 if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url) else 0

def count_digits(url):
    return sum(c.isdigit() for c in url)

def count_subdomains(url):
    domain_part = url.split('/')[0] if '//' not in url else url.split('//')[1].split('/')[0]
    return domain_part.count('.')

suspicious_words = ['login', 'verify', 'secure', 'account', 'update', 'bank', 'confirm', 'signin']
def has_suspicious_word(url):
    url_lower = url.lower()
    return 1 if any(word in url_lower for word in suspicious_words) else 0

def count_hyphens(url):
    return url.count('-')

suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.club']
def has_suspicious_tld(url):
    url_lower = url.lower()
    return 1 if any(url_lower.endswith(tld) or tld + '/' in url_lower for tld in suspicious_tlds) else 0

if st.button('Scan URL') and url_input:
    features = [[
        len(url_input),
        count_special_chars(url_input),
        has_ip(url_input),
        count_digits(url_input),
        count_subdomains(url_input),
        has_suspicious_word(url_input),
        count_hyphens(url_input),
        has_suspicious_tld(url_input)
    ]]
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.error('This URL looks malicious.')
    else:
        st.success('This URL looks safe.')