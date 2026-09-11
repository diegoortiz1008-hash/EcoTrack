import streamlit as st
from estimator import parse_and_estimate_co2

st.set_page_config(page_title="EcoTrack - Vibe MVP", page_icon="🌱", layout="centered")

st.title("🌱 EcoTrack")
st.caption("Registra tu impacto diario en lenguaje natural mediante Vibe Coding.")

user_input = st.text_area(
    "¿Qué hiciste hoy?",
    placeholder="Ejemplo: Hoy comí carne y viajé 20km en bus...",
    height=100
)

if st.button("Calcular Huella", type="primary"):
    if user_input.strip():
        result = parse_and_estimate_co2(user_input)
        
        st.subheader("📊 Resultado de tu Impacto")
        st.metric(label="Emisiones Totales Estimadas", value=f"{result['total_co2']} kg CO2")
        
        st.markdown("**Desglose de la actividad:**")
        for item in result["breakdown"]:
            st.write(f"- {item}")
    else:
        st.warning("Por favor ingresa una descripción de tus actividades.")