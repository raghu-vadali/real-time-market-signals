import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000/alerts"

st.set_page_config(page_title="Alerts Center", layout="wide")
st.title("🚨 Alerts Center")

symbols = st.text_input("Symbols", value="AAPL,MSFT,TSLA")

if st.button("Refresh"):
    r = requests.get(API_URL, params={"symbols": symbols})
    if r.status_code == 200:
        alerts = r.json()
        if alerts:
            df = pd.DataFrame(alerts)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No alerts triggered")
    else:
        st.error("API error")
