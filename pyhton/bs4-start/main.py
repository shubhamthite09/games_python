import requests
from bs4 import BeautifulSoup
responce = requests.get("https://news.ycombinator.com/news")
news_web = responce.text

soup = BeautifulSoup(news_web, "html.parser")
output = soup.find_all(name="a", class_="titlelink")
artical_texts= []
artical_links = []
for artical in output:
    arical_text= artical.getText()
    artical_texts.append(arical_text)
    artical_link = artical.get("href")
    artical_links.append(artical_link)

vote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

p = max(vote)
largest_vote = vote.index(p)
print(artical_texts[largest_vote])
print(artical_links[largest_vote])



