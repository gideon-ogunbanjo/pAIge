# pAIge
### Overview
pAIge is a machine learning model designed to classify different types of Iris flowers based on their sepal length, sepal width, petal length, and petal width. It uses the Random Forest Classifier algorithm to predict the type of iris based on the provided input features.

### Model Description:

pAIge is a supervised learning model that uses the Random Forest Classifier algorithm to predict the type of Iris based on the provided input features. The model is trained on a dataset of Iris flowers, with four input features (sepal length, sepal width, petal length, and petal width) and one output feature (the type of Iris). The dataset is split into training and testing sets, with 70% of the data used for training and 30% used for testing.

### Model Training:

During the training phase, the pAIge model learns to classify different types of Iris flowers based on the input features. The Random Forest Classifier algorithm is used to build a collection of decision trees, where each tree is trained on a subset of the training data. The model then combines the predictions of all the decision trees to make a final prediction. This method of combining predictions is known as ensemble learning, which allows for more accurate and stable predictions.

### Model Evaluation:

Once the model is trained, it is evaluated on the testing set to determine its performance. The performance of the pAIge model is measured using various metrics such as accuracy, precision, recall, and F1 score. The accuracy of the model is the percentage of correct predictions made by the model, while precision and recall measure the model's ability to correctly identify positive cases and negative cases, respectively. The F1 score is the harmonic mean of precision and recall, and it is used to balance the two metrics.

### Deployment:

pAIge is a Python-based model that can be deployed using streamlit. Once deployed, users can provide the input features (sepal length, sepal width, petal length, and petal width) to the model and receive a prediction of the type of Iris. To run just type `streamlit run app.py`

### Conclusion:

pAIge is a machine learning model designed to classify different types of Iris flowers based on their sepal length, sepal width, petal length, and petal width. It uses the Random Forest Classifier algorithm to predict the type of Iris based on the provided input features. The model is trained on a dataset of Iris flowers, and it is evaluated on various performance metrics. Once deployed, the model can be integrated into other applications to provide predictions of the type of Iris.

