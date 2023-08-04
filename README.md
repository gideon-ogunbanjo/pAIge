# pAIge - Iris Classification Model
### Overview
pAIge is an app that uses a RandomForestClassifier model to classify iris flowers into different species based on their sepal length, sepal width, petal length, and petal width. The app allows users to input values for these parameters using sliders and then predicts the iris flower species along with their prediction probabilities.

### Model Description
The RandomForestClassifier model is an ensemble learning method based on decision tree classifiers. It works by creating multiple decision tree models during training and outputs the class that is the mode of the classes (classification) or the mean prediction (regression) of the individual trees. Random forests help to reduce overfitting and improve generalization by combining multiple weak learners (trees) to form a strong learner.

In this application, the model is trained on the Iris dataset, which contains samples of three different species of iris flowers: Setosa, Versicolor, and Virginica. The model learns patterns from the features (sepal length, sepal width, petal length, and petal width) of these iris flowers and uses them to make predictions on new, unseen data.

### Model Deployment
pAIge is a Python-based model that has been deployed using streamlit. Users can provide the input features (sepal length, sepal width, petal length, and petal width) to the model and receive a prediction of the type of Iris. To use this mode visit

### Model Prediction
The app uses the well-known Iris dataset, which is built into the scikit-learn library. The dataset consists of 150 samples of iris flowers, each with four features (sepal length, sepal width, petal length, and petal width), and each sample is labeled with the species of iris it belongs to. A RandomForestClassifier model is created and trained on the Iris dataset using the provided features and labels. After inputting the parameters, the app will predict the species of iris flower based on the given input. The predicted species will be displayed below the "Iris Flower Prediction" subheader.

### Prediction Probability
The app will also display the prediction probabilities for each class, indicating the confidence of the model's predictions.
Labels of Class and their Respective Index Numbers: Under this section, you can see the class labels (species names) of iris flowers and their respective index numbers. The species names are as follows:
0: Setosa
1: Versicolor
2: Virginica

### Creator
Gideon Ogunbanjo