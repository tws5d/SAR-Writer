import streamlit as st
st.title("SAR Writer 🧠")

st.subheader("Select SAR Filing Reasons")
reason_source = st.checkbox("Suspicion concerning the source of funds")
reason_rapid = st.checkbox("Rapid movement of funds")
reason_no_purpose = st.checkbox("No reasonable economic, business, or lawful purpose")

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "csv"])

import pandas as pd

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
    date_a = date_b = None

    if uploaded_file:
        import pandas as pd
        try:
            # always reset file pointer before reading
            uploaded_file.seek(0)
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            # --- pull fields by name ---
            customer_name = str(df["Customer Name"].iloc[0])

            # --- get min and max from Transaction Date ---
            date_col = pd.to_datetime(df["Transaction Date"], errors="coerce").dropna()
            if not date_col.empty:
                date_a = date_col.min().strftime("%B %d, %Y")
                date_b = date_col.max().strftime("%B %d, %Y")
        except Exception as e:
            st.error(f"Error reading file: {e}")
            customer_name = None
    else:
        customer_name = None

    if customer_name or reasons:
        surname = customer_name.split()[-1] if customer_name else "[Customer Name Unavailable]"
        paragraph += f'Our Bank is filing this Suspicious Activity Report (SAR) on {customer_name or "[Customer Name Unavailable]"} ("{surname}")'

        if reasons:
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

            paragraph += f' due to {reason_text}'
        else:
            paragraph += '.'

        # --- add date range if available ---
        if date_a and date_b:
            if date_a == date_b:
                # Count distinct Transaction ID and sum Transaction Amount
                tx_count = df["Transaction ID"].nunique()
                tx_total = df["Transaction Amount"].sum()
                paragraph += f'. On {date_a}, {surname} conducted {tx_count} transactions totaling ${tx_total:,.2f}.'
            else:
                paragraph += f'. Between {date_a} and {date_b}.'
        else:
            paragraph += '.'
              
    else:
        paragraph = "No information available yet."

    st.write(paragraph)
