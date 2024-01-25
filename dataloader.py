# data_loader.py
import pandas as pd
import streamlit as st
import datetime

@st.cache_data
def load_data():
    dataset_url = 'https://raw.githubusercontent.com/Cikaryu/Paris-House-Price-Prediction/main/ParisHousing.csv'
    dataset = pd.read_csv(dataset_url)

    # Hitung ageOfProperty
    current_year = datetime.datetime.now().year
    dataset['ageOfProperty'] = current_year - dataset['made']

    return dataset