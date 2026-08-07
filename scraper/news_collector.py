import pandas as pd
from datetime import datetime


news_data = [

    {
        "title": "NAFDAC warns Nigerians about counterfeit medicines",
        "source": "NAFDAC",
        "date": "2026",
        "text": "NAFDAC continues efforts to prevent counterfeit drugs and promote medicine safety in Nigeria.",
        "topic_keyword": "counterfeit drugs"
    },

    {
        "title": "Experts warn against self medication and misuse of antibiotics",
        "source": "Channels TV",
        "date": "2026",
        "text": "Health experts advise Nigerians to avoid self medication and inappropriate antibiotic use.",
        "topic_keyword": "self medication"
    },

    {
        "title": "Drug safety concerns rise among Nigerian patients",
        "source": "Guardian Nigeria",
        "date": "2026",
        "text": "Healthcare professionals highlight the importance of safe medication practices.",
        "topic_keyword": "drug safety"
    }

]


df = pd.DataFrame(news_data)


df.to_csv(
    "data/NDSNC_2026_news.csv",
    index=False
)


print("Dataset created successfully!")
print(f"Articles collected: {len(df)}")