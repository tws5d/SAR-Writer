import streamlit as st
st.title("SAR Writer 🧠")

st.subheader("Select SAR Filing Reasons")
reason_source = st.checkbox("Suspicion concerning the source of funds")
reason_rapid = st.checkbox("Rapid movement of funds")
reason_no_purpose = st.checkbox("No reasonable economic, business, or lawful purpose")

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "csv"])
