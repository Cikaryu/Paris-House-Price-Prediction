import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from dataloader import load_data

@st.cache_data
def train_model(dataset):
    # Create a RandomForestRegressor model
    model = RandomForestRegressor()

    # Fit the model on the training data
    X_train = dataset[['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors', 'cityCode', 'cityPartRange', 'numPrevOwners', 'made', 'isNewBuilt', 'hasStormProtector', 'basement', 'attic', 'garage', 'hasStorageRoom', 'hasGuestRoom']]
    y_train = dataset['price']
    model.fit(X_train, y_train)

    return model, X_train.columns

def feature():
    st.title("Feature Selection")
    st.write("Selamat datang di bagian program aplikasi prediksi harga rumah di Paris.")
    
    # Memanggil fungsi load_data dengan caching
    dataset = load_data()

# Create a RandomForestRegressor model
    model, feature_columns = train_model(dataset)
# Get feature importances
    feature_importances = model.feature_importances_

# Display feature importances in a table
    st.subheader("Feature Importances:")
    feature_importance_df = pd.DataFrame({
        'Feature': feature_columns,
        'Importance': feature_importances
    })
    st.table(feature_importance_df)

# Correlation Analysis
    correlation_matrix = dataset.corr()

# Look at the correlations with the 'Price' column
    feature_correlation = correlation_matrix["price"].sort_values(ascending=False)

# Display feature correlations in a table
    st.subheader("Feature Correlations with Price:")
    feature_correlation_df = pd.DataFrame({
        'Feature': feature_correlation.index,
        'Correlation': feature_correlation.values
    })
    st.table(feature_correlation_df)

    # Scatter plot
    st.subheader("Scatter plot between price and squareMeters:")
    fig, ax = plt.subplots()
    sns.scatterplot(data=dataset, x="price", y="squareMeters", ax=ax)
    st.pyplot(fig)  # Display the scatter plot in Streamlit

if __name__ == "__main__":
    dataset = load_data
    feature(dataset)