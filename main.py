import streamlit as st
from streamlit_option_menu import option_menu
from dataexploration import explore

with st.sidebar:
    selected = option_menu(
        menu_title="Paris House Prediction",
        options=["Pengenalan","Data Exploration","Feature Selection","Feature Engineering","Data Splitting","Prediction"],
        menu_icon="cast",
        default_index = 0,  
    )
    if selected == "Pengenalan":
        st.title(f"Welcome to Paris House Prediction")
     
        st.markdown(
        """
        In this machine learning project to predict house prices in Paris using regression methods, we use the Linear Regression algorithm to identify the relationship between various property features (such as size, location, and number of rooms, age of the house, etc.) and house prices. 
        By utilizing a dataset that includes historical house data, the model learns to make price predictions based on certain characteristics. Once trained, the model can accept new inputs about the features of the house and produce an output in the form of a price estimate. 
        This output can provide valuable information to potential buyers, sellers, or homeowners to make more informed decisions in the context of the Paris real estate market.
    """
    )
    elif selected == "Data Exploration":
        explore()