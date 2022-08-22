from bs4 import BeautifulSoup as bs
import requests as rq
from IPython import embed
import re
import dateutil

URL = "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index"
page = rq.get(URL)
src = bs(page.content, 'lxml')
table = src.find('table')
rows = table.find_all('tr')

for row in rows[2:-1]:
    cells = row.find_all(['td', 'th']   )
    cell_text = [cell.get_text(strip=True) for cell in cells]
    rank, change, country, score, pstchange = cell_text
    #country = re.findall(r'[\w+ ]+', country)[0]
    try:
        pstchange = float(re.findall(r'\d.\d+', pstchange)[0])
    except:
        pstchange = 'NA'
    print(rank, country, score,pstchange)

embed()
