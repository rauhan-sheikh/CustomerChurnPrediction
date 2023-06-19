# Customer Churn Prediction App

Customer churn, or customer attrition, refers to the phenomenon where customers stop doing business with a company or stop using its services. Churn prediction plays a crucial role in helping businesses identify customers likely to churn, enabling proactive measures to retain them. The Customer Churn Prediction Streamlit App aims to provide businesses with a user-friendly interface to predict customer churn and understand the factors influencing it.

This repository contains a Streamlit app for customer churn prediction. The app allows users to input customer details and predicts whether a customer is likely to churn or not based on the provided information.

## [Streamlit App](https://rauhan-sheikh-customerchurnprediction-app-35g08h.streamlit.app/)

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

## Key Features:

- User-friendly Interface: The Streamlit app provides an intuitive interface where users can instantly input customer data and receive churn predictions.

- Data Input: Users can input customer-related information such as demographics, transaction history, usage patterns, and customer interactions. The app accepts these inputs and processes them to make accurate churn predictions.

- Churn Prediction: The predictive model implemented in the app analyzes the input data and generates churn predictions for individual customers. It utilizes machine learning algorithms and techniques such as SVM, XGBoost, RandomForest etc., to learn patterns from historical data and make reliable predictions.<br><br>

Overall, the Customer Churn Prediction Streamlit App provides businesses with an effective tool to predict customer churn and gain valuable insights into customer behaviour. By leveraging machine learning and interactive visualization, the app empowers businesses to make data-driven decisions and implement targeted strategies for customer retention.
