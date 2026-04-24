import streamlit as st
import pandas as pd
import joblib

# Cargar modelo (ajusta el nombre)
model = joblib.load("modelo_ataque_corazon.pkl")

st.title("Predicción de Riesgo de Ataque al Corazón")
st.write("Responde el siguiente cuestionario:")

# --- CUESTIONARIO ---
edad = st.slider("Edad", 18, 100, 40)

sexo = st.selectbox("Sexo", ["Masculino", "Femenino"])
sexo = 1 if sexo == "Masculino" else 0

cp = st.selectbox("Tipo de dolor en el pecho", [
    "Angina típica",
    "Angina atípica",
    "Dolor no anginoso",
    "Asintomático"
])

cp_map = {
    "Angina típica": 0,
    "Angina atípica": 1,
    "Dolor no anginoso": 2,
    "Asintomático": 3
}
cp = cp_map[cp]

trestbps = st.number_input("Presión arterial en reposo (mm Hg)", 80, 200, 120)
chol = st.number_input("Colesterol (mg/dl)", 100, 600, 200)

fbs = st.selectbox("¿Glucosa en ayunas > 120 mg/dl?", ["No", "Sí"])
fbs = 1 if fbs == "Sí" else 0

restecg = st.selectbox("Resultado ECG", [
    "Normal",
    "Anormalidad ST-T",
    "Hipertrofia ventricular"
])

restecg_map = {
    "Normal": 0,
    "Anormalidad ST-T": 1,
    "Hipertrofia ventricular": 2
}
restecg = restecg_map[restecg]

thalach = st.slider("Frecuencia cardíaca máxima", 60, 220, 150)

exang = st.selectbox("¿Angina inducida por ejercicio?", ["No", "Sí"])
exang = 1 if exang == "Sí" else 0

oldpeak = st.number_input("Depresión ST (oldpeak)", 0.0, 6.0, 1.0)

# --- BOTÓN ---
if st.button("Predecir riesgo"):
    
    data = pd.DataFrame([[
        edad, sexo, cp, trestbps, chol,
        fbs, restecg, thalach, exang, oldpeak
    ]], columns=[
        "age", "sex", "cp", "trestbps", "chol",
        "fbs", "restecg", "thalach", "exang", "oldpeak"
    ])
    
    pred = model.predict(data)[0]
    
    if pred == 1:
        st.error("Alto riesgo de ataque al corazón")
    else:
        st.success("Bajo riesgo de ataque al corazón")