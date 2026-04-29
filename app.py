import streamlit as st

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
    tab_flujo, tab_clases, tab_er, tab_secuencia = st.tabs([
        "Diagramas de Flujo", 
        "Diagramas de Clases", 
        "Entidad-Relación", 
        "Diagramas de Secuencia"
    ])

    # Sección: Diagramas de Flujo
    with tab_flujo:
        st.subheader("Flowcharts")
        st.info("Próximamente: Ejemplos de lógica algorítmica y procesos.")
        # Aquí insertaremos la lógica de la sección 1

    # Sección: Diagramas de Clases
    with tab_clases:
        st.subheader("Class Diagrams")
        st.info("Próximamente: Estructuras de Programación Orientada a Objetos.")
        # Aquí insertaremos la lógica de la sección 2

    # Sección: Diagramas de Entidad-Relación
    with tab_er:
        st.subheader("Entity Relationship Diagrams (ERD)")
        st.info("Próximamente: Modelado de bases de datos relacionales.")
        # Aquí insertaremos la lógica de la sección 3

    # Sección: Diagramas de Secuencia
    with tab_secuencia:
        st.subheader("Sequence Diagrams")
        st.info("Próximamente: Interacción entre objetos y flujos temporales.")
        # Aquí insertaremos la lógica de la sección 4

if __name__ == "__main__":
    main()