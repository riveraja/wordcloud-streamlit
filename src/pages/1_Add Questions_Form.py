import streamlit as st
from sqlalchemy.sql import text

# sqlite connection
conn = st.connection('sqlite3',type='sql',ttl=10)

@st.cache_data(ttl=0)
def get_questions():
    results = conn.query(f"SELECT question as 'Questions list' FROM questions")
    return results

# Start page render here

st.header("Add questions form")

with st.form('add_question_form'):
    c1, c2 = st.columns([3,1])

    with c1:
        question = st.text_input(label='add_question',placeholder='Write your question here...',label_visibility="collapsed")

    with c2:
        if st.form_submit_button('Add question'):
            if question == '':
                st.write("Question field is blank.")
            else:
                with conn.session as c:
                    c.execute(text(f"INSERT INTO questions (question) VALUES ('{question}');"))
                    c.commit()

with st.container():
    if st.button('Show all questions',use_container_width=True):
        st.table(get_questions())