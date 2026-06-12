import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="ApnaHire AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS — Modern Glassmorphism + Gradient Theme
# =====================================================
st.markdown("""
<style>

/* ---------- GLOBAL ---------- */
.stApp {
    background: radial-gradient(circle at 20% 20%, #1e1b4b 0%, #0f172a 45%, #020617 100%);
    color: #f1f5f9;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

/* Hide default streamlit chrome */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1224 0%, #111827 100%);
    border-right: 1px solid rgba(255,255,255,0.06);
}

section[data-testid="stSidebar"] .stRadio label {
    font-size: 16px;
    padding: 6px 0;
}

/* ---------- HERO BANNER ---------- */
.hero {
    background: linear-gradient(120deg, #4f46e5 0%, #7c3aed 45%, #06b6d4 100%);
    padding: 36px 40px;
    border-radius: 24px;
    margin-bottom: 28px;
    box-shadow: 0 10px 40px rgba(79, 70, 229, 0.35);
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: "";
    position: absolute;
    top: -50%;
    right: -10%;
    width: 300px;
    height: 300px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
    filter: blur(10px);
}

.big-title {
    font-size: 46px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -1px;
    margin-bottom: 6px;
}

.subtitle {
    font-size: 18px;
    color: rgba(255,255,255,0.88);
    font-weight: 400;
}

/* ---------- GLASS CARDS ---------- */
.card {
    background: rgba(255,255,255,0.05);
    padding: 24px;
    border-radius: 18px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    transition: all 0.25s ease;
}

.card:hover {
    border-color: rgba(124,58,237,0.5);
    transform: translateY(-2px);
}

/* ---------- METRIC CARDS ---------- */
div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 18px 20px;
    backdrop-filter: blur(12px);
    transition: all 0.25s ease;
}

div[data-testid="stMetric"]:hover {
    border-color: rgba(6,182,212,0.5);
    transform: translateY(-2px);
}

div[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 800;
}

/* ---------- SECTION HEADERS ---------- */
h1, h2, h3 {
    color: #f8fafc !important;
    font-weight: 800 !important;
}

.section-pill {
    display: inline-block;
    background: rgba(124,58,237,0.18);
    color: #c4b5fd;
    border: 1px solid rgba(124,58,237,0.35);
    padding: 4px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}

/* ---------- DATAFRAME ---------- */
div[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
}

/* ---------- INPUTS & BUTTONS ---------- */
.stTextInput input {
    background: rgba(255,255,255,0.06) !important;
    color: #f1f5f9 !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 12px !important;
    padding: 10px 14px !important;
}

.stButton button, .stDownloadButton button {
    background: linear-gradient(90deg, #4f46e5, #7c3aed) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 10px 24px !important;
    font-weight: 700 !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 16px rgba(124,58,237,0.35) !important;
}

.stButton button:hover, .stDownloadButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(124,58,237,0.5) !important;
}

/* ---------- FEATURE PILLS (About page) ---------- */
.feature-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 12px 18px;
    margin: 6px 0;
    font-size: 15px;
    width: 100%;
}

.tech-badge {
    display: inline-block;
    background: rgba(6,182,212,0.15);
    color: #67e8f9;
    border: 1px solid rgba(6,182,212,0.35);
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    margin: 4px 4px 4px 0;
}

/* ---------- DIVIDER ---------- */
hr {
    border-color: rgba(255,255,255,0.08) !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================
@st.cache_data
def load_data():
    return pd.read_csv("submission.csv")

df = load_data()

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 10px 0 24px 0;'>
        <div style='font-size:42px;'>🤖</div>
        <div style='font-size:22px; font-weight:800; color:#f8fafc;'>ApnaHire AI</div>
        <div style='font-size:13px; color:#94a3b8;'>Candidate Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

    menu = st.radio(
        "Navigation",
        ["🏠 Dashboard", "🔍 Candidate Explorer", "📈 Analytics", "ℹ️ About"],
        label_visibility="collapsed"
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:12px; color:#64748b; text-align:center;'>"
        "Built for Redrob Hackathon<br>Team ApnaHire</div>",
        unsafe_allow_html=True
    )

# =====================================================
# DASHBOARD
# =====================================================
if menu == "🏠 Dashboard":

    st.markdown("""
    <div class='hero'>
        <div class='big-title'>🤖 ApnaHire AI</div>
        <div class='subtitle'>Intelligent Candidate Discovery & Ranking Engine —
        powered by semantic search, career analysis and behavioral signals.</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👥 Candidates Ranked", f"{len(df):,}")

    with c2:
        st.metric("🏆 Top Score", round(df["score"].max(), 2))

    with c3:
        st.metric("📊 Average Score", round(df["score"].mean(), 2))

    with c4:
        st.metric("✅ Status", "Success")

    st.write("")
    st.markdown("<span class='section-pill'>LEADERBOARD</span>", unsafe_allow_html=True)
    st.subheader("🏆 Top 10 Candidates")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        height=400
    )

    csv = df.to_csv(index=False)

    st.download_button(
        "⬇️  Download Submission CSV",
        csv,
        "submission.csv",
        "text/csv"
    )

# =====================================================
# CANDIDATE EXPLORER
# =====================================================
elif menu == "🔍 Candidate Explorer":

    st.markdown("<span class='section-pill'>SEARCH</span>", unsafe_allow_html=True)
    st.title("🔍 Candidate Explorer")
    st.caption("Look up a specific candidate by ID to view their rank, score and reasoning.")

    col_input, col_btn = st.columns([4, 1])
    with col_input:
        candidate_id = st.text_input(
            "Enter Candidate ID",
            placeholder="CAND_0098846",
            label_visibility="collapsed"
        )
    with col_btn:
        search_clicked = st.button("Search Candidate", use_container_width=True)

    if search_clicked:

        result = df[df["candidate_id"].str.upper() == candidate_id.upper()]

        if result.empty:
            st.error(f"❌ Candidate '{candidate_id}' not found")
            st.info("Please enter a valid Candidate ID, e.g. CAND_0098846")

        else:
            row = result.iloc[0]

            st.write("")
            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("🏅 Rank", int(row["rank"]))

            with c2:
                st.metric("⭐ Score", round(row["score"], 2))

            with c3:
                st.metric("🆔 Candidate", row["candidate_id"])

            st.write("")
            st.markdown("<span class='section-pill'>WHY THIS CANDIDATE</span>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class='card'>
                {row['reasoning']}
            </div>
            """, unsafe_allow_html=True)

# =====================================================
# ANALYTICS
# =====================================================
elif menu == "📈 Analytics":

    st.markdown("<span class='section-pill'>INSIGHTS</span>", unsafe_allow_html=True)
    st.title("📈 Ranking Analytics")
    st.caption("Visual breakdown of candidate scores across the ranked dataset.")

    chart_template = "plotly_dark"
    accent_colors = ["#7c3aed", "#06b6d4", "#4f46e5", "#22d3ee", "#a78bfa"]

    fig = px.histogram(
        df,
        x="score",
        title="Score Distribution",
        nbins=30,
        template=chart_template,
        color_discrete_sequence=["#7c3aed"]
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#f1f5f9",
        title_font_size=18,
        bargap=0.05
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(
        df.head(20),
        x="candidate_id",
        y="score",
        title="Top 20 Candidates",
        template=chart_template,
        color="score",
        color_continuous_scale="Plasma"
    )
    fig2.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#f1f5f9",
        title_font_size=18,
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig2, use_container_width=True)

# =====================================================
# ABOUT
# =====================================================
elif menu == "ℹ️ About":

    st.markdown("<span class='section-pill'>ABOUT THE PROJECT</span>", unsafe_allow_html=True)
    st.title("ℹ️ About ApnaHire AI")

    st.markdown("""
    <div class='card' style='margin-bottom:20px;'>
    <h3 style='margin-top:0;'>Intelligent Candidate Discovery &amp; Ranking Engine</h3>
    ApnaHire AI combines semantic search, career history analysis, experience matching
    and behavioral signals to identify and rank the most relevant candidates for any
    job description.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<span class='section-pill'>FEATURES</span>", unsafe_allow_html=True)
        features = [
            "🧠 Semantic Search",
            "📈 Career History Analysis",
            "🎯 Experience Matching",
            "🔍 Behavioral Signal Scoring",
            "⚖️ Hybrid Ranking System"
        ]
        for f in features:
            st.markdown(f"<div class='feature-pill'>{f}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<span class='section-pill'>TECH STACK</span>", unsafe_allow_html=True)
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        techs = ["Python", "Pandas", "Plotly", "Streamlit", "Sentence Transformers", "Scikit-Learn"]
        badges = "".join([f"<span class='tech-badge'>{t}</span>" for t in techs])
        st.markdown(badges, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div class='card' style='text-align:center;'>
    <h3 style='margin-top:0;'>👨‍💻 Team ApnaHire</h3>
    Built for the Redrob Intelligent Candidate Discovery &amp; Ranking Challenge.
    </div>
    """, unsafe_allow_html=True)