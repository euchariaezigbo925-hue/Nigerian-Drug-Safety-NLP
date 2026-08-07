import pandas as pd
import os


file_path = "data/raw/NDSNC_raw_articles.csv"


new_articles = [

    {
        "title": "NAFDAC warns against counterfeit medicines",
        "source": "NAFDAC",
        "date": "2026",
        "text": "NAFDAC continues efforts to protect Nigerians from counterfeit and substandard medicines.",
        "url": "https://nafdac.gov.ng",
        "topic_keyword": "counterfeit drugs"
    },

    {
        "title": "Experts discuss medication safety in Nigeria",
        "source": "Health Report",
        "date": "2026",
        "text": "Healthcare professionals emphasize responsible medicine use and the dangers of unsafe self medication.",
        "url": "",
        "topic_keyword": "drug safety"
    }

]


new_df = pd.DataFrame(new_articles)


if os.path.exists(file_path):

    old_df = pd.read_csv(file_path)

    final_df = pd.concat(
        [old_df, new_df],
        ignore_index=True
    )

else:

    final_df = new_df


final_df.to_csv(
    file_path,
    index=False
)


print("Raw dataset updated!")
print("Total articles:", len(final_df))