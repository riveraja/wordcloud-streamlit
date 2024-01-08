import streamlit as st
from sqlalchemy.sql import text

st.set_page_config(page_title="Streamlit App", layout="wide")

# sqlite connection
conn = st.connection("sqlite3", type="sql", ttl=10)

with conn.session as c:
    c.execute(text("CREATE TABLE IF NOT EXISTS questions (question TEXT);"))
    c.execute(text("CREATE TABLE IF NOT EXISTS answers (qid INTEGER, answer TEXT);"))

st.title("Wordcloud")

st.markdown(
    """
    Testing wordcloud in streamlit with SQLite3 backend.

    Select a question from the sidebar.
"""
)
