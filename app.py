import streamlit as st
from views.flow_view import render_flowchart_section

# Configuración de la página
st.set_page_config(
    page_title="Visualizador de Diagramas Mermaid",
    page_icon="📊",
    layout="wide"
)

def main():
    # Header Principal
    st.header("📊 Ejemplos de diagramas con Mermaid 2")
    st.markdown("""
    Esta herramienta permite previsualizar y entender la sintaxis de diferentes 
    diagramas técnicos utilizados en la arquitectura de software y el diseño de sistemas.
    """)

    # Creación de los tabuladores (secciones)
    tabs = st.tabs([
        "Diagramas de Flujo", 
        "Diagramas de Clases", 
        "Entidad-Relación", 
        "Diagramas de Secuencia"
    ])

    # Sección: Diagramas de Flujo
    with tabs[0]:
        render_flowchart_section()

if __name__ == "__main__":
    main()