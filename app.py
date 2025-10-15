import streamlit as st
st.title("SAR Writer 🧠")

st.subheader("Select SAR Filing Reasons")
reason_source = st.checkbox("Suspicion concerning the source of funds")
reason_rapid = st.checkbox("Rapid movement of funds")
reason_no_purpose = st.checkbox("No reasonable economic, business, or lawful purpose")

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "csv"])

if st.button("Generate Paragraph"):
    st.subheader("Generated Paragraph")
    paragraph = "This SAR filing is based on observed activity that raised concerns regarding potential illicit financial behavior."
    
    reasons = []
    if reason_source:
        reasons.append("suspicion concerning the source of funds")
    if reason_rapid:
        reasons.append("rapid movement of funds")
    if reason_no_purpose:
        reasons.append("no reasonable economic, business, or lawful purpose")
    
    if reasons:
        paragraph += " The filing is primarily due to " + ", ".join(reasons) + "."
    
    st.write(paragraph)
