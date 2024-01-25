# import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st
from dataloader import load_data

@st.cache_data
def explore(dataset):
    st.title(f"Data Exploration and Loading")
    st.write("These steps involve understanding and preparing the Paris Housing Dataset before using it for further analysis or model training.")

    # Importing the dataset
    st.subheader("Dataset Preview:")
    st.write("The application fetches the dataset from a specified URL and displays a preview of the dataset's initial rows.")
    st.write(dataset.head())

    # Checking for missing values
    missing_values = dataset.isnull().sum()

# Display missing values in a table
    st.subheader("Missing Values:")
    st.write("It then checks for missing values in the dataset and presents a table summarizing the count of missing values for each feature.")
    missing_values_df = pd.DataFrame({
        'Feature': missing_values.index,
        'Missing Values': missing_values.values
    })
    st.table(missing_values_df)


    st.subheader("Distribution of House Prices:")
    st.write("To provide insights into the distribution of house prices, a histogram is generated and displayed using Matplotlib. This visualization helps users understand the frequency distribution of house prices in the dataset.")
    fig, ax = plt.subplots()
    ax.hist(dataset['price'], bins=60)
    ax.set_xlabel('price')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of House Prices')

# Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    dataset = load_data()
    explore(dataset)