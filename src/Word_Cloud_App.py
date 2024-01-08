import streamlit as st
from sqlalchemy.sql import text

st.set_page_config(page_title="Streamlit App", layout="wide")

st.title("Wordcloud")

st.markdown(
    """
    Testing wordcloud in streamlit with SQLite3 backend.

    Select a question from the sidebar.
"""
)
