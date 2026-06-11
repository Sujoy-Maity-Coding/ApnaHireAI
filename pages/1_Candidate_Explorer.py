import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Candidate Explorer",
    page_icon="🔍",
    layout="wide"
)

df = pd.read_csv("submission.csv")

st.title("🔍 Candidate Explorer")

candidate_id = st.text_input(
    "Enter Candidate ID",
    placeholder="Example: CAND_0098846"
)

if st.button("Search"):

    candidate = df[
        df["candidate_id"] == candidate_id
    ]

    if candidate.empty:

        st.error(
            f"❌ Candidate '{candidate_id}' not found."
        )

        st.info(
            "Please enter a valid Candidate ID from the ranking dataset."
        )

    else:

        row = candidate.iloc[0]

        col1,col2,col3 = st.columns(3)

        with col1:
            st.metric(
                "Rank",
                row["rank"]
            )

        with col2:
            st.metric(
                "Score",
                round(row["score"],2)
            )

        with col3:
            st.metric(
                "Candidate",
                row["candidate_id"]
            )

        st.subheader("🧠 AI Reasoning")

        st.success(
            row["reasoning"]
        )

        st.balloons()