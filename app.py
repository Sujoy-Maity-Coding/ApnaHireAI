import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ApnaHire AI",
    page_icon="🤖",
    layout="wide"
)

# Load Data
df = pd.read_csv("submission.csv")

# Header
st.title("🤖 ApnaHire AI")
st.subheader(
    "Intelligent Candidate Discovery & Ranking Engine"
)

st.markdown("---")

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Candidates Ranked",
        len(df)
    )

with col2:
    st.metric(
        "Top Match Score",
        round(df.iloc[0]["score"], 2)
    )

with col3:
    st.metric(
        "Ranking Engine",
        "Active"
    )

st.markdown("---")

# About
with st.expander("📌 Solution Overview"):

    st.write("""
    ApnaHire AI uses:

    • Semantic Search

    • Career History Analysis

    • Experience Matching

    • Behavioral Signal Scoring

    • Hybrid Ranking Engine

    to identify the most relevant candidates
    for AI engineering roles.
    """)

# Search
st.markdown("## 🔍 Search Candidate")

search = st.text_input(
    "Search Candidate ID"
)

if search:

    filtered = df[
        df["candidate_id"]
        .str.contains(
            search,
            case=False
        )
    ]

    st.dataframe(
        filtered,
        use_container_width=True
    )

else:

    st.markdown("## 🏆 Top Ranked Candidates")

    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )

st.markdown("---")

# Top Candidate
st.markdown("## ⭐ Best Candidate")

best = df.iloc[0]

st.write(
    f"Candidate ID: {best['candidate_id']}"
)

st.write(
    f"Rank: {best['rank']}"
)

st.write(
    f"Score: {round(best['score'],2)}"
)

st.write(
    f"Reasoning: {best['reasoning']}"
)

st.markdown("---")

# Download
csv = df.to_csv(index=False)

st.download_button(
    label="⬇ Download Ranked CSV",
    data=csv,
    file_name="submission.csv",
    mime="text/csv"
)

st.success(
    "Ranking Completed Successfully"
)