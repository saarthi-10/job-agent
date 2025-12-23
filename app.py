import streamlit as st
import pandas as pd
from db import get_db

st.set_page_config(page_title="Job Dashboard", layout="wide")
st.title("📊 Product & Analytics Jobs")

conn = get_db()
df = pd.read_sql("SELECT * FROM jobs ORDER BY first_seen DESC", conn)

st.dataframe(df, use_container_width=True)
