from bs4 import BeautifulSoup as soup
import re
src = open('hallo_world.html')
document = soup(src, 'lxml')
headers = document.find_all('h1')


for head in headers:
    text = head.get_text()
    new_text = re.sub('H.llo', 'Hei', text)
    print(new_text)
