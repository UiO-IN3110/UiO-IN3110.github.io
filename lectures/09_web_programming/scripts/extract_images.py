from bs4 import BeautifulSoup as soup
import requests as req
import re
from IPython import embed


URL = 'https://en.wikipedia.org/wiki/University_of_Oslo'

page = req.get(URL)
src = page.content
document = soup(src, 'lxml')

images = document.find_all('img')

new_images = []
for image in images:
    if 'class' in image.attrs:
        if image.attrs['class'] == ['thumbimage']:
            new_images.append(image.attrs['src'])


embed()


