import streamlit as st
st.title("SAR Writer 🧠")

st.subheader("Select SAR Filing Reasons")
reason_source = st.checkbox("Suspicion concerning the source of funds")
reason_rapid = st.checkbox("Rapid movement of funds")
reason_no_purpose = st.checkbox("No reasonable economic, business, or lawful purpose")

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "csv"])

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
            # Build reason text with "the" only before reasons that should have it
            formatted_reasons = []
            for r in reasons:
                if r.startswith("rapid"):
                    formatted_reasons.append(f"the {r}")
                else:
                    formatted_reasons.append(r)

            if len(formatted_reasons) == 1:
                reason_text = formatted_reasons[0]
            elif len(formatted_reasons) == 2:
                reason_text = f"{formatted_reasons[0]}, and {formatted_reasons[1]}"
            else:
                reason_text = ", ".join(formatted_reasons[:-1]) + f", and {formatted_reasons[-1]}"

            paragraph += f' due t
