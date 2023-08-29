import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
responce = requests.get(URL)
web_html = responce.text

soup = BeautifulSoup(web_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
#print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("top_100_movies.text", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")