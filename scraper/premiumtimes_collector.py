import pandas as pd
import os


premiumtimes_articles = [

    {
        "title": "Nigeria tackles growing challenge of counterfeit medicines",
        "source": "Premium Times",
        "date": "2026",
        "text": "Health authorities and stakeholders continue efforts to reduce the circulation of counterfeit and substandard medicines in Nigeria.",
        "url": "https://www.premiumtimesng.com",
        "topic_keyword": "counterfeit drugs"
    },

    {
        "title": "Experts highlight dangers of improper medication use",
        "source": "Premium Times",
        "date": "2026",
        "text": "Healthcare professionals emphasize the importance of proper medicine use and consultation with qualified healthcare providers.",
        "url": "https://www.premiumtimesng.com",
        "topic_keyword": "medication safety"
    },

    {
        "title": "Nigeria strengthens efforts against antimicrobial resistance",
        "source": "Premium Times",
        "date": "2026",
        "text": "Health stakeholders promote responsible antibiotic use to address antimicrobial resistance challenges.",
        "url": "https://www.premiumtimesng.com",
        "topic_keyword": "antibiotic resistance"
    }

]


new_df = pd.DataFrame(premiumtimes_articles)


file_path = "data/NDSNC_2026_news.csv"


if os.path.exists(file_path):

    old_df = pd.read_csv(file_path)

    combined_df = pd.concat(
        [old_df, new_df],
        ignore_index=True
    )

else:

    combined_df = new_df


combined_df.to_csv(
    file_path,
    index=False
)


print("Premium Times articles added!")
print("Total corpus size:", len(combined_df))