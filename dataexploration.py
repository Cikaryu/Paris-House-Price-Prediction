# import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Construct the file path using os.path.join
import streamlit as st

def explore():
    st.title(f"Data Exploration and Loading")
    st.write("Selamat datang di bagian program aplikasi prediksi harga rumah di Paris.")

    # Importing the dataset
    dataset = pd.read_csv(r'C:\Users\ASUS\Downloads\Newfolder\asc\Paris-House-Price-Prediction\ParisHousing.csv')
    st.subheader("Dataset Preview:")
    st.write(dataset.head())

    # Checking for missing values
    missing_values = dataset.isnull().sum()

# Display missing values in a table
    st.subheader("Missing Values:")
    missing_values_df = pd.DataFrame({
        'Feature': missing_values.index,
        'Missing Values': missing_values.values
    })
    st.table(missing_values_df)


    st.subheader("Distribution of House Prices:")
    fig, ax = plt.subplots()
    ax.hist(dataset['price'], bins=60)
    ax.set_xlabel('price')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of House Prices')

# Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    explore()
