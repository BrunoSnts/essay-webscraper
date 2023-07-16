from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

f = open("url.txt", "r")
a = open("out.txt", "a")
for i in range(3): ##range is to be number of urls
    essayPage = f.readline()
    req = Request(url=essayPage, headers={'User-Agent': 'Chrome/114.0.0.0'})
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    essay = soup.find("div", class_="article__content")
    extras = essay.findChildren("div", recursive=False)
    for Ediv in extras:
        essay.div.decompose()
    a.write(essay.text)
    a.write('')
