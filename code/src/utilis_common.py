import pandas as pd
import PyPDF2
from io import StringIO

def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df

def extract_text_from_pdf(uploaded_doc):
    reader = PyPDF2.PdfReader(uploaded_doc)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text
