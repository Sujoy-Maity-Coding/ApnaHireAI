import streamlit as st
import pandas as pd

st.set_page_config(page_title="ApnaHire AI")

st.title("ApnaHire AI")
st.subheader("Intelligent Candidate Discovery & Ranking Engine")

df = pd.read_csv("submission.csv")

st.write("Top Ranked Candidates")

st.dataframe(df)

csv = df.to_csv(index=False)

st.download_button(
    label="Download Submission CSV",
    data=csv,
    file_name="submission.csv",
    mime="text/csv"
)