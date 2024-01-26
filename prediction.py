# streamlit_predict_app.py
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
import datetime

def predict():
    # Load the dataset
    @st.cache_data
    def load_data():
        dataset = pd.read_csv(r'https://raw.githubusercontent.com/Cikaryu/Paris-House-Price-Prediction/main/ParisHousing.csv')
        current_year = datetime.datetime.now().year
        dataset['ageOfProperty'] = current_year - dataset['made']
        return dataset, current_year

    # Load data
    data, current_year = load_data()

    # User input for the new house details
    st.subheader("Enter New House Details")
    new_meters = st.number_input("Area of the new house (meters)", min_value=0.0, value=100.0, step=1.0)
    new_square_meters = new_meters ** 2
    new_number_of_rooms = st.number_input("Number of rooms", min_value=1, value=None, step=1,)
    option_has_yard = st.radio("Does the new house have a yard?", ["Yes", "No"])
    new_has_yard = 1 if option_has_yard == "Yes" else 0

    option_has_pool = st.radio("Does the new house have a pool?", ["Yes", "No"])
    new_has_pool = 1 if option_has_pool == "Yes" else 0
    
    new_floors = st.number_input("Number of floors", min_value=1, value=None, step=1)

    new_city_code = st.number_input("Enter the city code of the new house", min_value=1, value=None, step=1)

    new_city_part_range = st.number_input("Enter the city part range of the new house", min_value=1, value=None, step=1)
    
    new_num_prev_owners = st.number_input("Enter the number of previous owners of the new house", min_value=1, value=None, step=1)

    new_construction_year = st.number_input("Enter the construction year of the new house: ", min_value=1800, value=None, step=1)
    
    option_new_built = st.radio("Is the new house newly built?", ["Yes", "No"])
    new_is_new_built =  1 if option_new_built == "Yes" else 0

    option_has_storm_protector = st.radio("Does the new house have a storm protector?", ["Yes", "No"], index=0)
    new_has_storm_protector = 1 if option_has_storm_protector == "Yes" else 0
    
    new_basement = st.number_input("Enter the basement of the new house", min_value=1, value=None, step=1)

    new_attic = st.number_input("Enter the attic of the new house", min_value=1, value=1, step=1,)
    
    new_garage = st.number_input("Enter the garage of the new house", min_value=1, value=None, step=1)

    option_has_storage_room = st.radio("Does the new house have a storage room?", ["Yes", "No"], index=0)
    new_has_storage_room= 1 if option_has_storage_room == "Yes" else 0

    new_has_guest_room = st.number_input("Enter the guest room of the new house", min_value=1, value=None, step=1)
    
    if new_construction_year is not None:
        age_of_property = current_year - new_construction_year
    else:
    # Provide a default value or handle the case where construction year is not provided
        age_of_property = 0

    # Create a DataFrame for the new house features
    new_house_features = pd.DataFrame({
        'squareMeters': [new_square_meters],
        'numberOfRooms': [new_number_of_rooms],
        'hasYard': [new_has_yard],
        'hasPool': [new_has_pool],
        'floors': [new_floors],
        'cityCode': [new_city_code],
        'cityPartRange': [new_city_part_range],
        'numPrevOwners': [new_num_prev_owners],
        'made': [new_construction_year],
        'isNewBuilt': [new_is_new_built],
        'hasStormProtector': [new_has_storm_protector],
        'basement': [new_basement],
        'attic': [new_attic],
        'garage': [new_garage],
        'hasStorageRoom': [new_has_storage_room],
        'hasGuestRoom': [new_has_guest_room],
        'ageOfProperty': [age_of_property]
    })

    # Display user input
    st.subheader("User Input:")
    st.write(new_house_features)
    # Predict the house price
    st.subheader("Predicted House Price:")

    # Add a "Predict" button
    if st.button("Predict"):
        with st.spinner("Predicting..."):
            # Create a RandomForestRegressor model
            model = RandomForestRegressor()
            X_train_columns = ['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors', 'cityCode', 'cityPartRange',
                            'numPrevOwners', 'made', 'isNewBuilt', 'hasStormProtector', 'basement', 'attic', 'garage',
                            'hasStorageRoom', 'hasGuestRoom', 'ageOfProperty']

            X_train = data[X_train_columns]  # Include 'ageOfProperty' in the training data
            y_train = data['price']
            model.fit(X_train, y_train)

            # Apply SimpleImputer to the new house features
            imputer = SimpleImputer(strategy='mean')
            imputer.fit(data[X_train_columns])  # Use the same columns as in X_train
            new_house_features_imputed = imputer.transform(new_house_features[X_train_columns])
            
            # Make predictions
            predicted_price = model.predict(new_house_features_imputed)
            st.write(f"The Predicted Price: € {predicted_price[0]:.2f}")

if __name__ == "__main__":
    predict()
