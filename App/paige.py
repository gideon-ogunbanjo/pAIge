import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# Streamlit app title
st.title("pAIge - Iris Classification Model")

# Sidebar for user input
st.sidebar.header('Input Parameters')
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

# Gets user input and display it
df = user_input_features()
st.subheader('Inputed parameters')
st.write(df)

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# Creates and trains the RandomForestClassifier model
clf = RandomForestClassifier()
clf.fit(X, Y)

# Makes predictions using the user input data
prediction = clf.predict(df.values)  # Convert DataFrame to NumPy array using .values
prediction_proba = clf.predict_proba(df.values)  # Convert DataFrame to NumPy array using .values

# Displays the class labels and their respective index numbers
st.subheader('Labels of Class and their respective index numbers')
st.write(iris.target_names)

# Displays the predicted iris flower species
st.subheader('Iris Flower Prediction')
st.write(iris.target_names[prediction])

# Displays the prediction probabilities for each class
st.subheader('Prediction Probability')
st.write(prediction_proba)

# Footer
st.markdown("Created by Gideon Ogunbanjo")