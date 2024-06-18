from bs4 import BeautifulSoup
import requests


data = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(data.text, "html.parser")
all_data = soup.find_all(class_="titleline")
title = all_data[0].find("a").text
score = soup.find_all(class_="score")

for num in range(len(all_data)-1):
    title = all_data[num].find("a").text
    web = all_data[num].find(class_="sitestr").text
    puntuation = score[num].text
    print(f"Title: {title}\nWeb: {web}\nScore: {puntuation}\n")