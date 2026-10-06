import streamlit as st
import pickle

# Load model
model = pickle.load(open("diabete_model", "rb"))

st.title("Diabetes Progression Prediction")

st.write("Enter the patient information:")

age = st.number_input("Age", value=0.0)
sex = st.number_input("Sex", value=0.0)
bmi = st.number_input("BMI", value=0.0)
bp = st.number_input("Blood Pressure", value=0.0)
s1 = st.number_input("S1", value=0.0)
s2 = st.number_input("S2", value=0.0)
s3 = st.number_input("S3", value=0.0)
s4 = st.number_input("S4", value=0.0)
s5 = st.number_input("S5", value=0.0)
s6 = st.number_input("S6", value=0.0)

if st.button("Predict"):

    input_data = [[
        age, sex, bmi, bp, s1, s2, s3, s4, s5, s6
    ]]
 
    prediction = model.predict(input_data)[0]

    st.metric("Predicted disease progression", f"{prediction:.2f}")

    if prediction < 100:
     st.success("🟢 Lower model-based risk")
    elif prediction < 200:
     st.warning("🟡 Moderate model-based risk")
    else:
     st.error("🔴 Higher model-based risk")

st.info(
    "This risk level is based on the model's predicted disease-progression "
    "score. It is not a medical diagnosis."
)