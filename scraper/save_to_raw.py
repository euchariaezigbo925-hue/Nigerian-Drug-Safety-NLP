import pandas as pd
import os


RAW_FILE = "data/raw/NDSNC_raw_articles.csv"


def save_articles(article_list):

    new_df = pd.DataFrame(article_list)

    if os.path.exists(RAW_FILE):

        old_df = pd.read_csv(RAW_FILE)

        final_df = pd.concat(
            [old_df, new_df],
            ignore_index=True
        )

    else:

        final_df = new_df


    final_df.drop_duplicates(
        subset=["title"],
        inplace=True
    )


    final_df.to_csv(
        RAW_FILE,
        index=False
    )


    print("Articles saved successfully!")
    print("Total articles:", len(final_df))