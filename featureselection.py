import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

@st.cache_data
def load_data():
    return pd.read_csv(r'https://raw.githubusercontent.com/Cikaryu/Paris-House-Price-Prediction/main/ParisHousing.csv')

def feature():
    st.title("Feature Selection")
    st.write("Welcome to the feature selection section of our Paris House Price Prediction application! In this part, we are preparing to build a model that can predict house prices based on various features. Let me walk you through what's happening:.")
    
    # Memanggil fungsi load_data dengan caching
    dataset = load_data()

# Create a RandomForestRegressor model
    model = RandomForestRegressor()

# Fit the model on the training data
    X_train = dataset[['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors', 'cityCode', 'cityPartRange', 'numPrevOwners', 'made', 'isNewBuilt', 'hasStormProtector', 'basement', 'attic', 'garage', 'hasStorageRoom', 'hasGuestRoom']]
    y_train = dataset['price']
    model.fit(X_train, y_train)
# Get feature importances
    feature_importances = model.feature_importances_

# Display feature importances in a table
    st.subheader("Feature Importances:")
    st.write("The application analyzes the importance of each feature in predicting house prices. The 'Feature Importances' table displays the contribution of each feature to the predictive power of the model. This information helps us understand which features play a significant role in determining house prices.")
    feature_importance_df = pd.DataFrame({
        'Feature': X_train.columns,
        'Importance': feature_importances
    })
    st.table(feature_importance_df)

# Correlation Analysis
    correlation_matrix = dataset.corr()

# Look at the correlations with the 'Price' column
    feature_correlation = correlation_matrix["price"].sort_values(ascending=False)

# Display feature correlations in a table
    st.subheader("Feature Correlations with Price:")
    st.write("We explore the correlation between different features and the house prices. The 'Feature Correlations with Price' table shows how strongly each feature correlates with the price. High correlations indicate strong relationships.")
    feature_correlation_df = pd.DataFrame({
        'Feature': feature_correlation.index,
        'Correlation': feature_correlation.values
    })
    st.table(feature_correlation_df)

    # Scatter plot
    st.subheader("Scatter plot between price and squareMeters:")
    st.write("To provide a visual representation, we display a scatter plot between house prices and the square footage of houses. This plot gives an intuitive sense of how the price varies with the size of the property.")
    fig, ax = plt.subplots()
    sns.scatterplot(data=dataset, x="price", y="squareMeters", ax=ax)
    st.pyplot(fig)  # Display the scatter plot in Streamlit

if __name__ == "__main__":
    feature()