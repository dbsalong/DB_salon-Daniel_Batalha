import streamlit as st
import pandas as pd

st.title("💇‍♀️ Gestión Peluquería")

# --- MENÚ LATERAL ---
menu = st.sidebar.selectbox("Ir a:", ["Agenda", "Stock", "Caja/Gastos"])

if menu == "Agenda":
    st.header("📅 Agenda del Día")
    st.write("Escribe el nombre de la clienta y la hora")
    # Aquí puedes añadir una tabla simple
    df_agenda = pd.DataFrame({"Hora": ["09:00", "10:00", "11:00"], "Clienta": ["", "", ""]})
    st.table(df_agenda)

elif menu == "Stock":
    st.header("📦 Control de Tintes y Productos")
    st.info("Aviso: Si queda menos de 3, saldrá en rojo.")

elif menu == "Caja/Gastos":
    st.header("💰 Caja y Gastos (IVA)")
    st.write("Registra tus servicios aquí para el gestor.")

