# Customer Churn Prediction App

This repository contains a Streamlit app for customer churn prediction. The app allows users to input customer details and predicts whether a customer is likely to churn or not based on the provided information.

## Streamlit App

The Streamlit app can be accessed [here](https://rauhan-sheikh-customerchurnprediction-app-35g08h.streamlit.app/). It provides a user-friendly interface to input customer details and obtain churn predictions.

The Streamlit app provides a user-friendly interface to interact with the customer churn prediction model. It prompts the user to enter various customer details such as gender, senior citizen status, partner, dependents, tenure, phone service, internet service, and more. After providing the necessary information, the user can click the "Predict" button to get the churn prediction result.

The app utilizes a pre-trained machine learning model, loaded from the `pipeline.pkl` file, to make the churn predictions. The input data is preprocessed to match the pipeline's requirements before making the prediction.


## Files

The repository includes the following files:

- [app.py](./app.py): The main Python script that defines the Streamlit app and handles the prediction functionality.
- [customer-churn-prediction-in-telecommunications.ipynb](./customer-churn-prediction-in-telecommunications.ipynb): Jupyter Notebook containing the data exploration, preprocessing, model training, and evaluation steps.
- [logo.png](./logo.png): A logo image representing the app, showcasing a human walking out.
- [WA_Fn-UseC_-Telco-Customer-Churn.csv](./WA_Fn-UseC_-Telco-Customer-Churn.csv): dataset used for model training and testing.
- `pipeline.pkl`: Pickled machine learning pipeline object containing preprocessing and classification steps.
