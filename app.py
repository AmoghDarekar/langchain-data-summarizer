import streamlit as st
import pandas as pd
from summarizer import summarize_big_data

st.set_page_config(page_title="AI Data Summarizer")
st.title("🚖 AI-Powered Big Data Summarizer")

uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Sample of uploaded data:", df.head())

    if st.button("Generate Summary"):
        with st.spinner("Summarizing using LangChain + OpenAI..."):
            summary = summarize_big_data(df)
        st.success("✅ Summary Generated:")
        st.markdown(summary)
