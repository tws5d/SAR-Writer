import streamlit as st
st.title("SAR Writer 🧠")

st.subheader("Select SAR Filing Reasons")
reason_source = st.checkbox("Suspicion concerning the source of funds")
reason_rapid = st.checkbox("Rapid movement of funds")
reason_no_purpose = st.checkbox("No reasonable economic, business, or lawful purpose")

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "csv"])

import pandas as pd

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("✅ File loaded successfully!")
    st.write(df.head())
    st.write("Columns detected:", list(df.columns))

if st.button("Generate SAR Intro"):
    st.subheader("Generated SAR Intro")

    # collect reasons first
    reasons = []
    if reason_source:
        reasons.append("suspicion concerning the source of funds")
    if reason_rapid:
        reasons.append("rapid movement of funds")
    if reason_no_purpose:
        reasons.append("no reasonable economic, business, or lawful purpose")

    paragraph = ""
    if uploaded_file:
        import pandas as pd
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            customer_name = str(df.iloc[0, 5])
        except Exception as e:
            st.error(f"Error reading file: {e}")
            customer_name = None
    else:
        customer_name = None

    if customer_name or reasons:
        paragraph += f'Our Bank is filing this Suspicious Activity Report (SAR) on {customer_name or "[Customer Name Unavailable]"}'

        if reasons:
            formatted_reasons = []
