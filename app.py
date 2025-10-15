import streamlit as st
st.title("SAR Writer 🧠")

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "csv"])
