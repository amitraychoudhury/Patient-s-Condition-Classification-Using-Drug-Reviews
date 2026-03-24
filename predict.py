import joblib

# Load the trained pipeline model
model = joblib.load("final_model.pkl")


def predict_condition(drug_text, review_text):
    """
    This function takes drug name and review text,
    combines them exactly like training,
    and returns predicted condition.
    """

    # Combine inputs (same format used during training)
    combined_input = (drug_text + " " + review_text).strip()

    # If user enters nothing
    if combined_input == "":
        return "Please enter a drug name or patient review."

    # Predict using trained pipeline
    prediction = model.predict([combined_input])[0]

    return prediction