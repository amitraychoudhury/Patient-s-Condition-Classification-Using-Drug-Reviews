import streamlit as st
from predict import predict_condition

# Page configuration
st.set_page_config(page_title="Patient Condition Classifier")

# Title
st.title("💊 Patient Condition Classification")

st.write(
    "This application predicts the patient's medical condition "
    "based on the drug name, patient review, or both."
)

# Inputs
drug = st.text_input("Enter Drug Name")
review = st.text_area("Enter Patient Review")

# Button
if st.button("Predict Condition"):

    result = predict_condition(drug, review)

    if result == "Please enter a drug name or patient review.":
        st.warning(result)
    else:
        st.success("Predicted Condition:")
        st.markdown(f"<h1 style='text-align:center; color:black;'>{result}</h1>", unsafe_allow_html=True)