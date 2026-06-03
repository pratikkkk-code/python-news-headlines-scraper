import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2")

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines, start=1):
            text = headline.get_text(strip=True)

            if text:
                file.write(f"{i}. {text}\n")

    print("Headlines saved to headlines.txt")

else:
    print("Failed to fetch webpage.")