import streamlit as st
import pandas as pd
from utilis_common import load_data, extract_text_from_pdf
from rule_generation import generate_profiling_rules
from anomaly_detection import detect_anomalies
from config import OPENAI_API_KEY

# Set OpenAI API key
import openai
openai.api_key = OPENAI_API_KEY

st.title('Data Profiling and Anomaly Detection App')

# Upload dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=['csv'])
if uploaded_file:
    df = load_data(uploaded_file)
    st.write("Data Preview:", df.head())

    # Upload regulatory document
    uploaded_doc = st.file_uploader("Upload the regulatory document (PDF)", type=['pdf'])
    if uploaded_doc:
        regulatory_text = extract_text_from_pdf(uploaded_doc)

        # Generate Profiling Rules
        if st.button('Generate Profiling Rules'):
            rules = generate_profiling_rules(regulatory_text)
            st.write("Generated Rules:", rules)

        # Anomaly Detection
        if st.button('Detect Anomalies'):
            anomalies = detect_anomalies(df)
            st.write("Anomalies Detected:", anomalies)
