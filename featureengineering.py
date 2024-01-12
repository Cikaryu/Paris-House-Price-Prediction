import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

# Membuat fungsi untuk membaca data dengan caching
@st.cache_data
def load_data():
    return pd.read_csv(r'C:\Users\ASUS\Downloads\Newfolder\asc\Paris-House-Price-Prediction\ParisHousing.csv')

def engine():
    st.title("Feature Engineering")
    st.write("Selamat datang di bagian program aplikasi prediksi harga rumah di Paris.")
    
    # Memanggil fungsi load_data dengan caching
    dataset = load_data()

    import datetime
    current_year=datetime.datetime.now().year
    dataset['ageOfProperty']=current_year - dataset['made']
    st.write(dataset.head())

if __name__ == "__main__":
    engine()