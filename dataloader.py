# data_loader.py
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    dataset_url = 'https://raw.githubusercontent.com/Cikaryu/Paris-House-Price-Prediction/main/ParisHousing.csv'
    return pd.read_csv(dataset_url)