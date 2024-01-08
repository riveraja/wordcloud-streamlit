import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sqlalchemy.sql import text

st.session_state.clicked = False

# sqlite connection
conn = st.connection("sqlite3", type="sql", ttl=10)


@st.cache_data(ttl=0)
def get_qid(q):
    res = conn.query(f"SELECT ROWID FROM questions WHERE question LIKE '{q}'")
    return res.iloc[0].values[0]


@st.cache_data(ttl=0)
def get_response(qid):
    response = conn.query(
        f"SELECT answer, count(*) as cnt FROM answers WHERE qid = {qid} GROUP BY qid,answer;"
    )
    return response


@st.cache_data(ttl=0)
def render_cloud(qid):
    response = get_response(qid)

    my_dict = {}
    for _i in range(len(response)):
        wrd = f"{response['answer'][_i]}"
        cnt = int(response["cnt"][_i])
        my_dict[wrd] = cnt

    if len(my_dict) > 0:
        word = WordCloud().generate_from_frequencies(my_dict)

        plt.imshow(word, interpolation="bilinear")
        plt.axis("off")
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0, 0)
        st.set_option("deprecation.showPyplotGlobalUse", False)
        st.pyplot(bbox_inches="tight", pad_inches=0)


# Page render starts here.
questions = conn.query("SELECT question FROM questions ORDER BY ROWID;")
st.header("Select a question")
option = st.selectbox(
    "Select your question", questions, index=0, label_visibility="collapsed"
)

with st.container():
    if st.button("Add a reply", use_container_width=True):
        qid = get_qid(option)

        c1, c2 = st.columns([3, 1])

        with c1:
            answer: str = ""
            qid = ""
            t_input = st.empty()
            answer = t_input.text_input(
                label="input",
                label_visibility="collapsed",
                placeholder="Reply goes here...",
            )

        with c2:
            if st.button("Add a reply"):
                st.session_state.clicked = True

                if answer != "" and st.session_state.clicked == True:
                    with conn.session as c:
                        c.execute(
                            text(
                                f"INSERT INTO answers (qid, answer) VALUES ('{qid}','{answer}')"
                            )
                        )
                        c.commit()

    if st.button(label="Render Cloud", use_container_width=True):
        qid = get_qid(option)
        render_cloud(qid)
