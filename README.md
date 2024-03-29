
# Paris House Price Prediction

Machine learning project to predict house prices in Paris using regression methodsmachine learning project to predict house prices in Paris using regression methods.
We want a machine learning model that can predict house prices based on factors such as location, size, amenities, etc. over time.

### The ideal outcome we want from our ML?
The ideal outcome of a house price prediction model is to provide price estimates that are close to or reflect the actual price of the house based on certain features such as the number of rooms, land area, location, and others.
We want our model to provide near-accurate and informative predictions, helping potential users make smart decisions in the sale or purchase of a home. The ultimate goal is to have a model that can provide a near-accurate price prediction or reflect the actual price of a home.

### How will we know if the ML system has failed?
Our success metric is how easily can users (potential home sellers and buyers) interact with this machine learning system to find out house price predictions so that users can understand and trust the prediction results. And these predictions can help users make decisions about buying and selling houses in the area.

Our ML model is considered unsuccessful if the results are not accurate with the actual house price data and are slow in generating price predictions

### The desired output results of the Machine Learning (ML) model to be built.
The desired output of this machine learning model is the house price in Euro which can provide a predicted value that is close to the actual price. 

Here is an example of the output that can be generated by this machine learning model: Predicted price of the house : € 1003895.76

## System Architecture (TechStack)

The following is the system architecture or tech stack that we consider to develop a house price prediction system using the Paris housing price prediction dataset

### Programming Language
Python : Used for data processing, analysis, and modeling.

### Framework and Library
•   Jupyter Notebook       : For experiments and data analysis.

•   Pandas                 : For data manipulation.

•   NumPy                  : For numerical operations.

•   Scikit-learn           : For house price prediction modeling.

•   Matplotlib and Seaborn : For data visualization.

### Machine Learning Model
Using regression or ensemble algorithms such as Random Forest or Gradient Boosting to build house price prediction models.

### UI Prototyping
Streamlit : For creating interactive and fast user interfaces.

## Configuration instructions
To run the Paris house price prediction project, you need to configure your working environment. Here are the steps:

### 1. Python installation
Make sure you have Python installed on your computer. If not, you can download it from the [official Python website](https://www.python.org/downloads/) and follow the installation guide.

### 2. Virtual Environment Creation 

It is recommended to create a virtual environment first to isolate the dependencies of this project. You can use virtualenv, [conda](https://www.anaconda.com/download), or [MiniConda](https://docs.conda.io/projects/miniconda/en/latest/) as per your preference.

#### Using virtualenv:

Mac / Linux :
```
$ pip3 install virtualenv
$ virtualenv myenv
$ source myenv/bin/activate
```

Windows :
```
PS:C/> pip install virtualenv
PS:C/> virtualenv myenv
PS:C/> myenv\Scripts\activate
```

Using Conda or MiniConda : 
```
(Base)C:/> conda create --name myenv python=3.7
(Base)C:/> conda activate myenv
```

### 3. Dependency Installation
In your working environment, install the required dependencies by running the following command:
```
$ pip install -r requirements.txt
```

### 4. Using Jupyter Notebook
You can run Jupyter Notebook to explore the data and experiment with our model. By using Visual Studio code with the ipynb extension or you can open it through a browser on [google coolab](https://colab.research.google.com/)

### 5. Streamlit
The Streamlit app has been prepared for user interaction. You can install it by running the following command:
```
$ pip install streamlit
```

After running the above command, and there is no error. means streamlit has been installed successfully. You can try it by running the following command:
```
$ streamlit --version 
$ streamlit hello
```
To run our project with streamlit. You can try it by running the following command:

```
$ cd ProjectLocation
$ streamlit run main.py
```

## App usage instructions

Once open your web browser and go to the URL [provided](https://parishousepredict.streamlit.app/).

You will be presented with the Introduction view, on the right there are also several sidebar options. Starting from Introduction, Prediction and Data exploration.

To use the Prediction feature, you can select the Prediction menu in the sidebar and the Prediction page will be displayed.

Enter the house details that must be inputted such as Area of the new house (meters), Number of rooms, Number of floors, etc.

After inputting all the house details, at the bottom there will be User input. user input contains a table that displays the user input above it. 

Click the Prediction button to get house price predictions in Paris. The price will be displayed in Euro currency.


## Contributor
Gung Satria (210040072)

Krisna Prasetya (210040038)

Juliana Putra (210040076)



