import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ApnaHire AI",
    page_icon="🤖",
    layout="wide"
)

df = pd.read_csv("submission.csv")

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg,#4F46E5,#06B6D4);
    padding:30px;
    border-radius:20px;
    color:white;
}
.metric-card {
    background:#111827;
    padding:15px;
    border-radius:15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>🤖 ApnaHire AI</h1>
<h3>Intelligent Candidate Discovery & Ranking Engine</h3>
</div>
""", unsafe_allow_html=True)

st.write("")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Candidates Ranked",
        len(df)
    )

with col2:
    st.metric(
        "Top Score",
        round(df["score"].max(),2)
    )

with col3:
    st.metric(
        "Ranking Status",
        "Success"
    )

st.divider()

st.subheader("🏆 Top 10 Candidates")

st.dataframe(
    df.head(10),
    use_container_width=True
)

csv = df.to_csv(index=False)

st.download_button(
    "⬇ Download Submission CSV",
    csv,
    "submission.csv",
    "text/csv"
)

st.success("Ranking Engine Running Successfully")