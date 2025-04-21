import streamlit as st
import json
from pickle import load

# Cargar el modelo
with open(r"C:\Users\mafer\OneDrive\Escritorio\Data Science\machine-learning-python-template--MFGS-Regularized-Linear-Models\src\Regularized_Linear_Lasso_.sav", 'rb') as f:
    model = load(f)

# Cargar el JSON que tiene los estados y su codificación
with open("state_name_transformation_rules.json", 'r') as json_file:
    transformation_rules = json.load(json_file)

st.title("Predicciones sobre tu salud")

# Como el JSON en sí es el diccionario, usamos directamente sus claves
opciones = list(transformation_rules.keys())

# Desplegable con los estados
seleccion = st.selectbox("Selecciona tu estado:", opciones)

# Obtener el valor codificado para ese estado
val3 = transformation_rules[seleccion]

# Sliders
val1 = st.slider("Edad", min_value=0.0, max_value=90.0, step=1.0)
val2 = st.slider("Peso (kg)", min_value=0.0, max_value=200.0, step=1.0)

# Diccionario de clases de salida (esto lo puedes ajustar según tu modelo)
class_dict = {
    "0": "No hay riesgo",
    "1": "Riesgo leve",
    "2": "Riesgo alto"
}

# Botón de predicción
if st.button("Predecir"):
    prediction = str(model.predict([[val1, val2, val3]])[0])
    pred_class = class_dict.get(prediction, "Desconocido")
    st.write("Predicción:", pred_class)
