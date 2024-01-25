import streamlit as st
from streamlit_option_menu import option_menu
from dataexploration import explore
from featureselection import feature
from dataloader import load_data
with st.sidebar:
    selected = option_menu(
        menu_title="Paris House Prediction",
        options=["Introduction","Predict","Data Exploration","Feature Selection"],
        menu_icon="cast",
        default_index = 0,  
    )
if selected == "Introduction":
    st.title(f"Welcome to Paris House Prediction")

    image_url = "https://assets.kompasiana.com/items/album/2015/08/04/www-telegraph-co-uk-55c0663792937374048b4567.jpg?v=600&t=o?t=o&v=740&x=416"
    st.image(image_url, use_column_width=True)

    # Introduction
    st.markdown(
    """
    <div style="text-align: justify;">
        Welcome to our Paris House Price Prediction application! Our goal is to provide you with a powerful tool to 
        estimate housing prices in the beautiful city of Paris. Whether you are a potential homebuyer, investor, or 
        simply curious about the real estate market in Paris, our model is designed to assist you in making informed decisions.
    </div>
    """),

    # About App
    st.markdown("<h3 class='centered'>About the Application</h3>", unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: justify;">
        Our application utilizes advanced machine learning algorithms to analyze various factors influencing house prices 
        in Paris. By inputting specific features such as the number of rooms, square footage, and location, our model 
        generates accurate predictions to help you understand the market dynamics.
    </div>
    """,
    unsafe_allow_html=True)
    
    # How To Use
    st.markdown("<h3 class='centered'>How to Use the Prediction Feature</h3>", unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: justify;">
        Get personalized predictions for house prices by filling out the simple input form. Explore how changing 
        parameters such as the size of the property or its location can impact the estimated price. Our application 
        aims to empower you with the information needed to make confident decisions in the housing market.
    </div>
    """,
    unsafe_allow_html=True)
    
    # Stay Informed
    st.markdown("<h3 class='centered'>Stay Informed</h3>", unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: justify;">
        Stay up-to-date with the latest trends and developments in the Paris real estate scene. Our application 
        is not just a prediction tool but a comprehensive resource to keep you informed about the ever-evolving 
        landscape of property values in the city of lights.
    </div>
    """,
    unsafe_allow_html=True)

    # Start Exploring
    st.markdown("<h2 class='centered'>Start Exploring</h2>", unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: justify;">
        Ready to dive in? Begin your journey into the world of Parisian real estate by navigating through the different 
        sections of our application. Whether you're a first-time homebuyer or a seasoned investor, our goal is to make 
        your experience seamless and informative.
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown("<h5 class='centered'>Thank you for choosing Paris House Price Prediction. Let's explore the future of real estate together!</h5>", unsafe_allow_html=True)
    
    

elif selected == "Data Exploration":
    dataset = load_data()
    explore(dataset)
elif selected == "Feature Selection":
    dataset = load_data()
    feature()