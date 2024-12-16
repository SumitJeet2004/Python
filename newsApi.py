import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-27&sortBy=publishedAt&apiKey=5eac9f78c7784693aba353dc99481683"
r = requests.get(url)


print(r.text)


news = r.json()

# Check if the response contains an error
if r.status_code != 200:
    print(f"Error: {news.get('message', 'Failed to retrieve news')}")
else:
    # Check if 'articles' key exists in the response
    if "articles" in news:
        for article in news["articles"]:
            print(article["title"])
            print(article["description"])
            print("--------------------------------------")
    else:
        print("No articles found in the response.")
