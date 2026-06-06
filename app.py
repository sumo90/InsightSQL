import streamlit as st
import pandas as pd

from sql_generator import generate_sql
from db import execute_query

st.set_page_config(
    page_title="InsightSQL",
    page_icon="🍁",
    layout="wide"
)

st.title("🍁 InsightSQL")

st.markdown(
    "Natural Language → Business Insights | Ask questions about products, customers, orders and revenue."
)

question = st.text_input(
    "Ask a question"
)

if question:

    with st.spinner("Analyzing..."):

        sql = generate_sql(question)

        columns, rows = execute_query(sql)

    st.subheader("Generated SQL")

    st.code(sql, language="sql")

    st.subheader("Results")

    df = pd.DataFrame(
        rows,
        columns=columns
    )

    st.dataframe(
        df,
        use_container_width=True
    )