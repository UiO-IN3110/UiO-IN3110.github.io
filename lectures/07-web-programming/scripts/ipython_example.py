from bs4 import BeautifulSoup as soup
import requests as req
from IPython import embed

URL = 'https://en.wikipedia.org/wiki/University_of_Oslo'
page = req.get(URL)
src = page.content
document = soup(src, 'lxml')
embed()

