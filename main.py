import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Paris House Prediction",
        options=["Pengenalan","Data Exploration","Feature Selection","Feature Engineering","Data Splitting","Prediction"],
        menu_icon="cast",
        default_index = 0,  
    )