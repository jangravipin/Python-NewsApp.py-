import requests

query = "artificial intelligence"
api = "2a13fffccd0f452d841077db21cafdb1"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-05-17&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate (articles):
    print(index + 1, article["title"], article["url"])
    print("\n**************************\n")