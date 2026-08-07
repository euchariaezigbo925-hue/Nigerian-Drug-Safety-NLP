import streamlit as st
import pandas as pd
from pathlib import Path

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Nigerian Drug Safety Intelligence",
    page_icon="💊",
    layout="wide"
)


# ==========================================
# HEALTHCARE INTELLIGENCE THEME
# ==========================================

st.markdown(
"""
<style>

[data-testid="stAppViewContainer"] {
    background-color:#F8FAFC;
}

h1 {
    color:#0F2942 !important;
    font-weight:800;
}

h2, h3 {
    color:#0EA5E9 !important;
    font-weight:700;
}


div[data-testid="metric-container"] {

    background:white;
    border-radius:15px;
    padding:20px;
    border-left:5px solid #0EA5E9;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);

}


section[data-testid="stSidebar"] {
    background:#F1F5F9;
}


footer {
    visibility:hidden;
}

</style>
""",
unsafe_allow_html=True
)



# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():

    file_path = Path(
        "data/processed/NDSNC_raw_articles.csv"
    )

    df = pd.read_csv(file_path)

    # Clean topic names by removing accidental spaces
    df["topic_keyword"] = (
        df["topic_keyword"]
        .astype(str)
        .str.strip()
    )

    return df


df = load_data()


# ==========================================
# HEADER
# ==========================================

st.title(
    "💊 Nigerian Drug Safety Intelligence Dashboard"
)


st.write(
"""
An AI/NLP-powered platform for monitoring Nigerian drug safety news,
identifying emerging medicine risks, and uncovering public health insights
through natural language processing and topic intelligence.
"""
)


st.divider()



# ==========================================
# INTELLIGENCE SUMMARY CARDS
# ==========================================

st.subheader("🚀 Intelligence Summary")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "📰 Articles Analysed",
        len(df)
    )


with col2:

    st.metric(
        "🏥 News Sources",
        df["source"].nunique()
    )


with col3:

    st.metric(
        "🧠 Safety Themes",
        df["topic_keyword"].nunique()
    )


with col4:

    st.metric(
        "🔍 Records Available",
        len(df)
    )



# ==========================================
# DATASET INTELLIGENCE
# ==========================================

st.divider()

st.subheader(
    "📊 Dataset Intelligence Overview"
)


st.info(
"""
This dashboard analyses Nigerian drug safety news using Artificial
Intelligence and Natural Language Processing (NLP). It identifies major
medicine safety themes, monitors drug-related discussions, and extracts
health intelligence insights.
"""
)



# ==========================================
# DATA PREVIEW
# ==========================================

st.subheader(
    "🗂 News Dataset Preview"
)


st.dataframe(
    df.head(),
    use_container_width=True
)



# ==========================================
# TOPIC INTELLIGENCE
# ==========================================

st.subheader(
    "🧠 Drug Safety Topic Intelligence"
)

topic_counts = df["topic_keyword"].value_counts()

st.bar_chart(
    topic_counts,
)



# ==========================================
# SOURCE INTELLIGENCE
# ==========================================

st.subheader(
    "📰 News Source Intelligence"
)

source_counts = df["source"].value_counts()

st.bar_chart(
    source_counts,
)



# ==========================================
# TOPIC EXPLORER
# ==========================================

st.subheader(
    "🔍 Drug Safety Topic Explorer"
)


selected_topic = st.selectbox(
    "Select a drug safety topic:",
    df["topic_keyword"].unique()
)


filtered_df = df[
    df["topic_keyword"] == selected_topic
]


st.write(
    f"Showing articles related to: **{selected_topic}**"
)


st.dataframe(
    filtered_df[
        ["title", "source", "date", "url"]
    ],
    use_container_width=True
)



# ==========================================
# SEARCH
# ==========================================

st.subheader(
    "🔎 Search Drug Safety News"
)


search_term = st.text_input(
    "Enter keyword (example: counterfeit, NAFDAC, medicine)"
)


if search_term:

    search_results = df[
        df["text"].str.contains(
            search_term,
            case=False,
            na=False
        )
    ]


    st.write(
        f"Found {len(search_results)} matching articles"
    )


    st.dataframe(
        search_results[
            ["title", "source", "date", "url"]
        ],
        use_container_width=True
    )



# ==========================================
# NLP VISUALIZATIONS
# ==========================================

st.subheader(
    "📈 NLP Analysis Visualizations"
)


st.image(
    "Images/nigeria_drug_safety_topic_distribution.png",
    caption="Drug Safety Topic Distribution"
)


st.image(
    "Images/nigeria_wordcloud.png",
    caption="Drug Safety News Word Cloud"
)


st.image(
    "Images/nigeria_lda_topic_distribution.png",
    caption="LDA Topic Distribution"
)



# ==========================================
# ABOUT
# ==========================================

st.subheader(
    "ℹ️ About This Platform"
)


st.write(
"""
The Nigerian Drug Safety Intelligence Dashboard is an AI/NLP-powered
health information analysis platform designed to discover medicine safety
themes, monitor drug-related discussions, and support data-driven health
intelligence.

The platform applies topic modelling, keyword analysis, and text
exploration techniques to uncover patterns in Nigerian drug safety news.
"""
)


st.caption(
"© Chizix 2026 | Advancing health intelligence through AI, NLP, and data-driven insights."
)