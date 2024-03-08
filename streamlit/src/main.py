from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore
from vanna.ollama import Ollama

import streamlit as st


class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        Ollama.__init__(self, config=config)
        ChromaDB_VectorStore.__init__(self, config=config)


vn = MyVanna(
    config={"model": "mistral", "ollama_host": "http://ollama-llm:11434"}
)
vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")

if not st.session_state.get("trained"):
    df_ddl = vn.run_sql(
        "SELECT type, sql FROM sqlite_master WHERE sql is not null"
    )

    for ddl in df_ddl["sql"].to_list():
        vn.train(ddl=ddl)
    st.session_state["trained"] = True


my_question = st.session_state.get("my_question", default=None)
if my_question is None:
    my_question = st.text_input(
        "Ask me a question that I can turn into SQL", key="my_question"
    )
else:
    st.title(my_question)

    sql = vn.generate_sql(my_question)
    st.code(sql, language="sql")

    df = vn.run_sql(sql)

    st.dataframe(df, use_container_width=True)

    fig = vn.get_plotly_figure(
        plotly_code=vn.generate_plotly_code(
            question=my_question, sql=sql, df=df
        ),
        df=df,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.button(
        "Ask another question", on_click=lambda: st.session_state.clear()
    )
