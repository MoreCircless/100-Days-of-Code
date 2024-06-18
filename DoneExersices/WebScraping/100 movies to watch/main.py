import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

data = requests.get(url=URL)
f_data = BeautifulSoup(data.text, "html.parser" )
title = f_data.title
title = title.text.split("|")
movies = f_data.find_all("h3",class_= "title")

with open("DoneExersices/WebScraping/100 movies to watch/Top_100_movies.txt", "w") as txt:
    txt.write(f"{title[0]}\n")
    txt.write("\n")
    for movie in movies[::-1]:
        txt.write(f"{movie.text}\n")

print("Done!")