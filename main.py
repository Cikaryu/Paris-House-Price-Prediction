import streamlit as st
from streamlit_option_menu import option_menu
from dataexploration import explore
from featureselection import feature
from dataloader import load_data
with st.sidebar:
    selected = option_menu(
        menu_title="Paris House Prediction",
        options=["Introduction","Data Exploration","Feature Selection"],
        menu_icon="cast",
        default_index = 0,  
    )
if selected == "Introduction":
    st.title(f"Welcome to Paris House Prediction")

    image_url = "https://assets.kompasiana.com/items/album/2015/08/04/www-telegraph-co-uk-55c0663792937374048b4567.jpg?v=600&t=o?t=o&v=740&x=416"
    st.image(image_url, use_column_width=True)
     
    st.markdown(
    """
    <div style="text-align: justify;">
        In this machine learning project to predict house prices in Paris using regression methods, we use the Linear Regression algorithm to identify the relationship between various property features (such as size, location, and number of rooms, age of the house, etc.) and house prices. 
        By utilizing a dataset that includes historical house data, the model learns to make price predictions based on certain characteristics. Once trained, the model can accept new inputs about the features of the house and produce an output in the form of a price estimate. 
        This output can provide valuable information to potential buyers, sellers, or homeowners to make more informed decisions in the context of the Paris real estate market.
    </div>
    """,
    unsafe_allow_html=True
)

elif selected == "Data Exploration":
    dataset = load_data()
    explore(dataset)
elif selected == "Feature Selection":
    dataset = load_data()
    feature()