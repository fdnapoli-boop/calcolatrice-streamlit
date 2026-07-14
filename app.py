"""Interfaccia web della calcolatrice Streamlit."""

import streamlit as st

from task_app.calculator import calculate


st.set_page_config(page_title="Calcolatrice", page_icon="🧮", layout="centered")

st.title("🧮 Calcolatrice")
st.write("Inserisci due numeri, scegli un'operazione e calcola il risultato.")

operation_labels = {
    "Somma (+)": "+",
    "Sottrazione (−)": "-",
    "Moltiplicazione (×)": "*",
    "Divisione (÷)": "/",
}

with st.form("calculator_form"):
    first_column, second_column = st.columns(2)
    with first_column:
        first_number = st.number_input("Primo numero", value=0.0)
    with second_column:
        second_number = st.number_input("Secondo numero", value=0.0)

    selected_operation = st.selectbox(
        "Operazione",
        options=list(operation_labels),
    )
    submitted = st.form_submit_button("Calcola", type="primary", use_container_width=True)

if submitted:
    try:
        result = calculate(
            first_number,
            second_number,
            operation_labels[selected_operation],
        )
    except ZeroDivisionError as error:
        st.error(str(error))
    else:
        st.success(f"Risultato: {result:g}")

