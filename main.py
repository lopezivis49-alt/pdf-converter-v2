import streamlit as st
import tempfile
import os

st.set_page_config(page_title="PDF to Word", layout="wide")
st.title("🔥 PDF → Word **GRATIS**")

st.markdown("""
**¡Funciona 100% en móvil!** 📱
- Sube PDF
- Convierte a Word editable
- Descarga instantánea
""")

# File uploader
uploaded_file = st.file_uploader("📤 **Arrastra PDF aquí**", type="pdf")

if uploaded_file is not None:
    st.success(f"✅ **{uploaded_file.name}** ({uploaded_file.size/1024:.0f}KB)")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("**🚀 CONVERTIR**", type="primary", use_container_width=True):
            with st.spinner("🔄 Procesando tu PDF..."):
                try:
                    # Método cloud-friendly
                    import pdfplumber
                    
                    # Preview primera página
                    with pdfplumber.open(uploaded_file) as pdf:
                        if pdf.pages:
                            st.image(pdf.pages[0].to_image(resolution=72).original, 
                                    caption="**Preview página 1**")
                    
                    # Conversión
                    from pdf2docx import Converter
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_pdf:
                        tmp_pdf.write(uploaded_file.read())
                        tmp_pdf_path = tmp_pdf.name
                    
                    cv = Converter(tmp_pdf_path)
                    cv.convert("output.docx")
                    cv.close()
                    os.unlink(tmp_pdf_path)
                    
                    # Descarga
                    with open("output.docx", "rb") as f:
                        st.download_button(
                            label="📥 **¡WORD LISTO!**",
                            data=f.read(),
                            file_name=f"{uploaded_file.name.replace('.pdf','')}_word.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )
                    
                    st.success("🎉 **¡Conversión exitosa!**")
                    st.balloons()
                    
                except ImportError as e:
                    st.error("❌ Librería faltante. Usa **Microsoft Lens** (gratis)")
                except Exception as e:
                    st.error(f"❌ {str(e)}")
    
    st.markdown("---")
    st.info("**iPhone**: Safari → Añadir pantalla inicio")

