import requests as rq
from bs4 import BeautifulSoup as soup
from IPython import embed

URL = "https://en.wikipedia.org/w/index.php"
title = "University_Of_Oslo"
oldid = 1005595395

params = {"title": title, "oldid": oldid}

page = rq.get(URL, params)
src = page.content
document = soup(src, "lxml")
embed()
