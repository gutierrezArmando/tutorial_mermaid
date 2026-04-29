import streamlit as st

from .utils import load_mmd

def render_flowchart_section():
    st.subheader("Visualizador de Diagramas de Flujo")
    
    # Cargamos el código desde el archivo externo
    initial_code = load_mmd("diagrams/flow_basico.mmd")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        flow_code = st.text_area("Editor Mermaid:", value=initial_code, height=300)
    
    with col2:
        if flow_code:
            # En lugar de st.mermaid, usamos markdown con el tag de mermaid
            st.write("Utilizando **st.markdown**")
            st.markdown(f"```mermaid\n{flow_code}\n```")
            st.divider()
            st.write("Utilizando **st.code**")
            st.code(flow_code, language="mermaid")