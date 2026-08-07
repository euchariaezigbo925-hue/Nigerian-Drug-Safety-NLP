import pandas as pd
from datetime import datetime
import os


# Master storage
articles = []


def add_article(title, source, date, text, url, topic_keyword):

    articles.append({

        "title": title,
        "source": source,
        "date": date,
        "text": text,
        "url": url,
        "topic_keyword": topic_keyword,
        "date_collected": datetime.now()

    })


# ==========================
# SAMPLE STRUCTURE
# (We will replace with real collected articles)
# ==========================


add_article(
    "NAFDAC warns Nigerians against counterfeit medicines",
    "NAFDAC",
    "2026",
    "NAFDAC continues monitoring and regulation of medicines to prevent fake drugs in Nigeria.",
    "https://nafdac.gov.ng",
    "counterfeit drugs"
)


add_article(
    "Experts warn about antibiotic misuse",
    "Channels TV",
    "2026",
    "Health experts advise Nigerians against self medication and improper antibiotic use.",
    "https://www.channelstv.com",
    "self medication"
)


# Convert to dataframe

df = pd.DataFrame(articles)


# Create data folder if missing

os.makedirs("../data", exist_ok=True)


# Save dataset

df.to_csv(
    /data/NDSNC_2026_news.csv",
    index=False
)


print("NDSNC-2026 corpus updated!")
print("Articles:", len(df))