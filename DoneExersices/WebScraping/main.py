from bs4 import BeautifulSoup
#import lxml

with open("DoneExersices/WebScraping/website.html") as data:
    content = data.read()


soup = BeautifulSoup(content, "html.parser")

tags = soup.find_all(name="a")
print(tags)

for tag in tags:
    print(tag.get("href"))



heading = soup.find(name="h1", id="name")


print(heading)

section = soup.find(name="h3", class_="heading")
print(section.get("class"))


company_url = soup.select_one(selector="p a")
print(company_url)


name = soup.select(selector=".heading")
print(name)