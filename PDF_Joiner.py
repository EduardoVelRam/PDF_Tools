import streamlit as st
import PyPDF2

# Variables
output_pdf = "documents/combined_pdf.pdf"

# Functions

def combine_pdfs(output_path, documents):

    combined_pdf = PyPDF2.PdfMerger()

    for document in documents:
        combined_pdf.append(document)

    combined_pdf.write(output_path) # Save the combined PDF to the specified output path


# Frontend
st.image("assets/combine_pdf.png")
st.header("Combine PDF Files")
st.subheader("Upload multiple PDF files to combine them into a single PDF.")

uploaded_pdfs = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

join = st.button(label="Join PDFs")


if join:

    if len(uploaded_pdfs) < 1:
        st.warning("Please upload at least two PDF files to combine.")
    else:
        combine_pdfs(output_pdf, uploaded_pdfs)
        st.success("PDF files combined successfully!")
        with open(output_pdf, "rb") as file:
            pdf_data = file.read()
        st.download_button(label="Download Combined PDF", data=pdf_data, file_name="combined_pdf.pdf")