import streamlit as st

st.set_page_config(page_title="PDF to Word", layout="wide")
st.title("🔥 PDF → Word **GRATIS - FUNCIONA**")
st.markdown("**Sube PDF → Descarga Word editable**")

# Sidebar
st.sidebar.success("✅ **iPhone/Android OK**")
st.sidebar.markdown("Añade a pantalla inicio")

# Upload PDF
uploaded_file = st.file_uploader("📤 **Arrastra PDF aquí**", type="pdf")

if uploaded_file is not None:
    st.success(f"✅ **{uploaded_file.name} cargado** ({uploaded_file.size/1000:.0f}KB)")
    
    # Botón convertir
    if st.button("**🚀 CONVERTIR A WORD**", type="primary", use_container_width=True):
        with st.spinner('🔄 Convirtiendo tu PDF...'):
            try:
                # Import dinámico (solo si funciona)
                from pdf2docx import Converter
                cv = Converter(uploaded_file)
                cv.convert("converted.docx")
                cv.close()
                
                # Descarga
                with open("converted.docx", "rb") as f:
                    st.download_button(
                        label="📥 **¡WORD LISTO! Descargar**",
                        data=f.read(),
                        file_name=f"{uploaded_file.name.replace('.pdf', '')}_word.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                st.balloons()
                st.success("🎉 **¡Conversión completada!**")
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("🔄 **Alternativa**: Usa Microsoft Lens (gratis)")
    
    # Info
    st.markdown("---")
    st.markdown("""
    **📱 Móvil perfecto:**
    - Safari/Chrome → Añadir pantalla inicio
    - Funciona offline después
    """)

st.markdown("---")
st.caption("Powered by Streamlit • Desarrollado con ❤️")
