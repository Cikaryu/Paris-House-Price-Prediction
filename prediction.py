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
        dataset = pd.read_csv(r'C:\Users\ASUS\Downloads\Newfolder\asc\Paris-House-Price-Prediction\ParisHousing.csv')
        current_year = datetime.datetime.now().year
        dataset['ageOfProperty'] = current_year - dataset['made']
        return dataset

    # Load data
    data = load_data()

    # Display the dataset
    st.title("Paris House Prediction")
    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    # User input for the new house details
    st.subheader("Enter New House Details")
    new_meters = st.number_input("Area of the new house (meters)", min_value=0.0, value=100.0, step=1.0)
    new_square_meters = new_meters ** 2
    new_number_of_rooms = st.number_input("Number of rooms", min_value=1, value=3, step=1)
    new_has_yard = st.radio("Does the new house have a yard?", [0, 1], index=0)
    new_has_pool = st.radio("Does the new house have a pool?", [0, 1], index=0)
    new_floors = st.number_input("Number of floors", min_value=1, value=2, step=1)

    new_city_code = st.text_input("Enter the city code of the new house (leave blank if not applicable): ")
    new_city_code = None if new_city_code.strip() == "" else int(new_city_code)

    new_city_part_range = st.text_input("Enter the city part range of the new house (leave blank if not applicable): ")
    new_city_part_range = None if new_city_part_range.strip() == "" else int(new_city_part_range)

    new_num_prev_owners = st.text_input("Enter the number of previous owners of the new house (leave blank if not applicable): ")
    new_num_prev_owners = None if new_num_prev_owners.strip() == "" else int(new_num_prev_owners)

    new_construction_year = st.number_input("Enter the construction year of the new house: ", min_value=1800, value=2020, step=1)
    new_is_new_built = st.radio("Is the new house newly built?", [0, 1], index=0)
    new_has_storm_protector = st.radio("Does the new house have a storm protector?", [0, 1], index=0)
    new_basement = st.radio("Does the new house have a basement?", [0, 1], index=0)
    new_attic = st.radio("Does the new house have an attic?", [0, 1], index=0)
    new_garage = st.radio("Does the new house have a garage?", [0, 1], index=0)
    new_has_storage_room = st.radio("Does the new house have a storage room?", [0, 1], index=0)
    new_has_guest_room = st.radio("Does the new house have a guest room?", [0, 1], index=0)
    new_ageOfProperty = st.number_input("Enter the age of the new house in years: ", min_value=0, value=1, step=1)

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
        'ageOfProperty': [new_ageOfProperty]
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
