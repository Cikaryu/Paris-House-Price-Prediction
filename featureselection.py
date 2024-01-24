import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

@st.cache_data
def load_data():
    return pd.read_csv(r'https://raw.githubusercontent.com/Cikaryu/Paris-House-Price-Prediction/main/ParisHousing.csv')