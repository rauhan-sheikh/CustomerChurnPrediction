import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# Load the pickled model
pipeline = joblib.load('pipeline.pkl')

# Define the dropdown options
gender_options = ['Male', 'Female']
senior_citizen_options = [0, 1]
yes_no_options = ['Yes', 'No']
phone_service_options = ['Yes', 'No']
multiple_lines_options = ['Yes', 'No', 'No phone service']
internet_service_options = ['DSL', 'Fiber optic', 'No']
internet_service_dependent_options = ['Yes', 'No', 'No internet service']
contract_options = ['Month-to-month', 'One year', 'Two year']
billing_options = ['Yes', 'No']
payment_method_options = ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']

# Set page config
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="auto"
)

# Load logo image
logo = Image.open("logo.png")
st.sidebar.image(logo, use_column_width=True)

# Create the Streamlit app
def main():
    st.title("Customer Churn Prediction")
    st.subheader("Please enter the customer details:")

    # Input fields
    gender = st.selectbox("Gender", gender_options)
    senior_citizen = st.selectbox("Senior Citizen", senior_citizen_options)
    partner = st.selectbox("Partner", yes_no_options)
    dependents = st.selectbox("Dependents", yes_no_options)
    tenure = st.number_input("Tenure", min_value=0)
    phone_service = st.selectbox("Phone Service", phone_service_options)
    multiple_lines = st.selectbox("Multiple Lines", multiple_lines_options)
    internet_service = st.selectbox("Internet Service", internet_service_options)
    online_security = st.selectbox("Online Security", internet_service_dependent_options)
    online_backup = st.selectbox("Online Backup", internet_service_dependent_options)
    device_protection = st.selectbox("Device Protection", internet_service_dependent_options)
    tech_support = st.selectbox("Tech Support", internet_service_dependent_options)
    streaming_tv = st.selectbox("Streaming TV", internet_service_dependent_options)
    streaming_movies = st.selectbox("Streaming Movies", internet_service_dependent_options)
    contract = st.selectbox("Contract", contract_options)
    paperless_billing = st.selectbox("Paperless Billing", billing_options)
    payment_method = st.selectbox("Payment Method", payment_method_options)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
    total_charges = st.number_input("Total Charges", min_value=0.0)

    # Predict button
    if st.button("Predict"):
        # Preprocess the input data
        input_data = {
            'gender': [gender],
            'SeniorCitizen': [senior_citizen],
            'Partner': [partner],
            'Dependents': [dependents],
            'tenure': [tenure],
            'PhoneService': [phone_service],
            'MultipleLines': [multiple_lines],
            'InternetService': [internet_service],
            'OnlineSecurity': [online_security],
            'OnlineBackup': [online_backup],
            'DeviceProtection': [device_protection],
            'TechSupport': [tech_support],
            'StreamingTV': [streaming_tv],
            'StreamingMovies': [streaming_movies],
            'Contract': [contract],
            'PaperlessBilling': [paperless_billing],
            'PaymentMethod': [payment_method],
            'MonthlyCharges': [monthly_charges],
            'TotalCharges': [total_charges]
        }

        df = pd.DataFrame(input_data)
        df['SeniorCitizen'] = df['SeniorCitizen'].astype('object')

        # Make prediction using the loaded model
        prediction = pipeline.predict(df)

        # Show the prediction
        st.subheader("Prediction:")
        if prediction[0] == 0:
            st.error("Churn: Yes")
        else:
            st.success("Churn: No")

# Run the app
if __name__ == '__main__':
    main()
