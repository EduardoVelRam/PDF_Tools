import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

st.title("Desbloquear PDF")

uploaded_file = st.file_uploader("Sube un PDF", type="pdf")

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)
    writer = PdfWriter()

    # copiar páginas
    for page in reader.pages:
        writer.add_page(page)

    # aplicar cifrado sin restringir permisos
    writer.encrypt(user_password="", owner_password=None)

    output_pdf = io.BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)

    st.success("PDF procesado correctamente")

    st.download_button(
        label="Descargar PDF desbloqueado",
        data=output_pdf,
        file_name="pdf_desbloqueado.pdf",
        mime="application/pdf"
    )