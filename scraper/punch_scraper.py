import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


keywords = [
    "drug safety",
    "fake drugs",
    "counterfeit medicine",
    "self medication",
    "NAFDAC",
    "drug overdose",
    "antibiotic resistance"
]


articles = []


def scrape_punch(keyword):

    url = f"https://punchng.com/?s={keyword.replace(' ', '+')}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    print(response.status_code)
    print(soup.title)

    for item in soup.select("article"):

        title = item.find("h2")

        if title:

            title_text = title.get_text(strip=True)

            link = title.find("a")["href"]

            articles.append({
                "title": title_text,
                "url": link,
                "source": "Punch",
                "keyword": keyword,
                "date_collected": datetime.now()
            })
for keyword in keywords:

    print(f"Searching Punch for: {keyword}")
    scrape_punch(keyword)


df = pd.DataFrame(articles)


df.to_csv(
    "data/punch_drug_news.csv",
    index=False
)


print("DONE!")
print(f"Collected {len(df)} articles")