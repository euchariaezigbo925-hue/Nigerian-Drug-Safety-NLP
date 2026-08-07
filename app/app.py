import streamlit as st
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Nigerian Drug Safety Intelligence",
    page_icon="💊",
    layout="wide"
)

# Title
st.title("💊 Nigerian Drug Safety Intelligence Dashboard")

st.write(
    """
    An AI/NLP-powered platform for analyzing Nigerian drug safety news,
    identifying major themes, and uncovering medicine safety insights.
    """
)


# Load dataset

@st.cache_data
def load_data():
    file_path = Path("data/processed/NDSNC_raw_articles.csv")
    df = pd.read_csv(file_path)
    return df


df = load_data()


# Dataset Overview

st.subheader("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📰 Articles Analyzed",
        len(df)
    )

with col2:
    st.metric(
        "🏥 News Sources",
        df["source"].nunique()
    )

with col3:
    st.metric(
        "🧠 Topics Identified",
        df["topic_keyword"].nunique()
    )


# Dataset Preview

st.subheader("🗂️ News Dataset Preview")

st.dataframe(df.head())


# Topic Distribution

st.subheader("🧠 Drug Safety Topic Distribution")

topic_counts = df["topic_keyword"].value_counts()

st.bar_chart(topic_counts)


# News Source Distribution

st.subheader("📰 News Source Distribution")

source_counts = df["source"].value_counts()

st.bar_chart(source_counts)


# Topic Explorer

st.subheader("🔍 Drug Safety Topic Explorer")

selected_topic = st.selectbox(
    "Select a drug safety topic:",
    df["topic_keyword"].unique()
)

filtered_df = df[df["topic_keyword"] == selected_topic]

st.write(
    f"Showing articles related to: **{selected_topic}**"
)

st.dataframe(
    filtered_df[
        ["title", "source", "date", "url"]
    ]
)


# Keyword Search

st.subheader("🔎 Search Drug Safety News")

search_term = st.text_input(
    "Enter keyword (example: counterfeit, NAFDAC, medicine)"
)

if search_term:

    search_results = df[
        df["text"]
        .str.contains(
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
        ]
    )


# Footer

st.divider()

st.caption(
    "Nigerian Drug Safety NLP Intelligence Platform | AI-powered health information analysis"
)
# NLP Visualizations

st.subheader("📈 NLP Analysis Visualizations")

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

# Project Information

st.divider()

st.subheader("ℹ️ About This Platform")

st.write(
    """
    The Nigerian Drug Safety Intelligence Dashboard is an AI/NLP-powered
    health information analysis tool designed to identify medicine safety
    themes, monitor drug-related discussions, and uncover insights from
    Nigerian health news sources.

    The platform applies natural language processing techniques including
    topic modelling, keyword analysis, and text-based exploration to support
    medicine safety intelligence.
    """
)

st.caption(
    "Built for AI-powered health intelligence research and data-driven decision support. © 2026 NextGen Chizix"
)