import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Membuat fungsi untuk membaca data dengan caching
@st.cache_data
def load_data():
    return pd.read_csv(r'C:\Users\ASUS\Downloads\Newfolder\asc\Paris-House-Price-Prediction\ParisHousing.csv')

def selection():
    st.title("Model Selection")
    st.write("Selamat datang di bagian program aplikasi prediksi harga rumah di Paris.")
    
    # Memanggil fungsi load_data dengan caching
    dataset = load_data()

    import datetime
    current_year=datetime.datetime.now().year
    dataset['ageOfProperty']=current_year - dataset['made']
    from sklearn.model_selection import train_test_split
    # we Define our features (X) and target variable (y)
    X = dataset.drop(columns=['price'])  # Features
    y = dataset['price']  # Target variable
    
    # we Split the data into training (80%) and testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    from sklearn.linear_model import LinearRegression
    # Create a Linear Regression model
    model = LinearRegression()
    
    X = X.rename(columns={0: 'feature_1', 1: 'feature_2'})
    
    # Train the model on the training data
    model.fit(X_train, y_train)
    st.subheader("Model Training:")
    st.markdown("```python\n{}\n```".format(repr(model)))

    from sklearn.metrics import mean_absolute_error, mean_squared_error
    # Make predictions on the testing data
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    # Display the evaluation metrics in Streamlit
    st.subheader("Model Evaluation:")
    evaluation_data = {
    'Metric': ['Mean Absolute Error', 'Mean Squared Error', 'Root Mean Squared Error'],
    'Value': [mae, mse, rmse]
    }
    evaluation_df = pd.DataFrame(evaluation_data)
    st.table(evaluation_df)

if __name__ == "__main__":
    selection()
