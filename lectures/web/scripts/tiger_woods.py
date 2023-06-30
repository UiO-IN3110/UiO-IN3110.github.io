import requests as req
from bs4 import BeautifulSoup as soup

URL = "https://en.wikipedia.org/wiki/Tiger_Woods"
page = req.get(URL)
src = page.content
document = soup(src, "lxml")

title = document.find(id="The_Players_Championship")
tables = title.find_all_next("table")

tournament_table = []
for table in tables:
    header = table.find("th").get_text(strip=True)
    if header == "Tournament":
        tournament_table.append(table)

tournament_table = tournament_table[0:2]
print(tournament_table)
