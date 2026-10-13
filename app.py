
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("diamond_price_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Diamond Price Prediction", page_icon="💎")

st.title("💎 Diamond Price Prediction")
st.write("Enter the diamond details to predict its price.")

# Get the original feature names
feature_names = list(model.feature_names_in_)

# Get the fitted preprocessing pipelines
preprocessor = model.named_steps["preprocessor"]

numerical_cols = []
categorical_cols = []
numerical_defaults = {}
categorical_options = {}

for name, transformer, columns in preprocessor.transformers_:
    if name == "num":
        numerical_cols = list(columns)
        imputer = transformer.named_steps["imputer"]

        numerical_defaults = dict(
            zip(numerical_cols, imputer.statistics_)
        )

    elif name == "cat":
        categorical_cols = list(columns)
        encoder = transformer.named_steps["encoder"]

        categorical_options = {
            col: list(categories)
            for col, categories in zip(
                categorical_cols, encoder.categories_
            )
        }

# Input form
with st.form("diamond_form"):
    inputs = {}

    st.subheader("Diamond Details")

    for col in feature_names:
        if col in numerical_cols:
            default = float(numerical_defaults[col])

            inputs[col] = st.number_input(
                f"Enter {col}",
                value=default
            )

        elif col in categorical_cols:
            options = categorical_options[col]

            inputs[col] = st.selectbox(
                f"Select {col}",
                options=options
            )

    submitted = st.form_submit_button("Predict Price")

if submitted:
    input_df = pd.DataFrame([inputs], columns=feature_names)
    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Diamond Price: {prediction:,.2f}")
