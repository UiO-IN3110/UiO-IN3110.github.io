from bs4 import BeautifulSoup as soup
import requests as rq
from IPython import embed
import re


URL = "https://en.wikipedia.org/w/index.php"
title = "University_Of_Oslo"
oldid = 1005595395

params = {"title":title, "oldid":oldid}

page = rq.get(URL, params)
src = page.content
document = soup(src, 'lxml')
embed()

