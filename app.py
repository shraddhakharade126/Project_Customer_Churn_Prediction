
import streamlit as st
import pandas as pd
import pickle


# Load model pipeline
with open('Coustomerchurn.pkl', 'rb') as f:
    cls = pickle.load(f)

st.title("Heart Disease Prediction")

st.write("Fill the details below :")
sinput_data = {
    'gender': st.number_input("Enter gender:(male=1,female=0) ",step=1),
    'SeniorCitizen': st.number_input("Enter SeniorCitizen or not (1=yes, 0=No): ",step=1),
    'Partner': st.number_input("Enter Partner (1=yes ,0=No) :",step=1),
    'PhoneService': st.number_input("Enter PhoneService(1=yes ,0=No) :",step=1),
    'MultipleLines': st.number_input("Enter MultipleLines (1=yes, 0=No): ",step=1),
    'Contract': st.number_input("Enter Contract (0-2):'Month-to-month': 0, 'One year': 1, 'Two year': 2 ",step=1),
    'PaymentMethod': st.number_input("Enter PaymentMethod (0-3 :Bank transfer': 0, 'Credit card': 1, 'Electronic check': 2, 'Mailed check': 3: ",step=1),
    'MonthlyCharges': st.number_input("Enter MonthlyCharges: "),
}

# Predict button
if st.button("Result"):
    user_df =pd.DataFrame([sinput_data])

    # Prediction
    try:
        log_pre= cls.predict(user_df)[0]        #st.success(f"Random Forest:", "Heart Disease " if tree_pre==1 else "No Heart Disease")
        if log_pre==1:
            st.write("The customer has cancelled or stopped using the service.")
        else:
            st.write("The customer continues to use and pay for the service")
    except Exception as e:
        st.error(f"Prediction failed: ")