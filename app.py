import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="ApnaHire AI",
    page_icon="🤖",
    layout="wide"
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#0f172a,
#111827,
#1e293b
);
color:white;
}

.hero{
background: linear-gradient(
90deg,
#4f46e5,
#06b6d4
);

padding:30px;
border-radius:25px;
margin-bottom:20px;
}

.card{
background: rgba(255,255,255,0.05);

padding:20px;

border-radius:20px;

backdrop-filter: blur(12px);

border:1px solid rgba(
255,
255,
255,
0.1
);
}

.big-title{
font-size:55px;
font-weight:800;
color:white;
}

.subtitle{
font-size:22px;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------

df = pd.read_csv("submission.csv")

# ---------- SIDEBAR ----------

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🔍 Candidate Explorer",
        "📈 Analytics",
        "ℹ️ About"
    ]
)

# ===================================
# DASHBOARD
# ===================================

if menu == "🏠 Dashboard":

    st.markdown("""
    <div class='hero'>
    <div class='big-title'>
    🤖 ApnaHire AI
    </div>

    <div class='subtitle'>
    Intelligent Candidate Discovery &
    Ranking Engine
    </div>
    </div>
    """,
    unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric(
            "Candidates Ranked",
            len(df)
        )

    with c2:
        st.metric(
            "Top Score",
            round(df["score"].max(),2)
        )

    with c3:
        st.metric(
            "Status",
            "Success"
        )

    st.divider()

    st.subheader("🏆 Top 10 Candidates")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        height=400
    )

    csv = df.to_csv(index=False)

    st.download_button(
        "⬇ Download Submission CSV",
        csv,
        "submission.csv",
        "text/csv"
    )