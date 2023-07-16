from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
req = Request(url='https://ivypanda.com/essays/subject/biology/',## replace with your own url
    headers={'User-Agent': 'Chrome/114.0.0.0'})
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")
info = soup.find_all("span", class_="taxonomy-meta__text")
Length = []
a = open("url.txt", "a")

x = 0
for i in info:
    wordcount = int(i.get_text())
    if(x%2 != 0):
        if(wordcount > 850):##replace with your own wordcount
            Length.append(True)
        else:
            Length.append(False)
    x+=1

links = []
for link in soup.findAll('a', class_="article__heading-link"):
    links.append(link.get('href'))

x = 0
for i in Length:
    if(i == True):
        a.write(links[x])
    x+=1


