import requests
from bs4 import BeautifulSoup as bs4
from pprint import pprint

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage_html = response.text

soup = bs4(webpage_html, "html.parser")
all_movies = soup.find_all("h3", class_="title")
movie_names = [movie.getText() for movie in all_movies]
movies = movie_names[::-1]

with open("movies.txt", mode="w",encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")