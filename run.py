import streamlit as st
import pypdf
from pypdf import PdfReader

st.header('PDF MERGER')
uploaded_files = st.file_uploader(
    "Choose PDF file", accept_multiple_files=True
)

merger = pypdf.PdfMerger()
for i in range(0,len(uploaded_files),1):
    merger.append(uploaded_files[i])

if st.button('MERGE'):
    merge_file = merger.write('sample.pdf')
    
    merger.close()
    #merge_file = 'sample.pdf'
    
    reader = PdfReader("sample.pdf")


with open("sample.pdf","rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="name.pdf",
        mime="pdf",
    )
