from bs4 import BeautifulSoup as soup
from IPython import embed

src = open("hello_world.html")
document = soup(src, "lxml")
headers = document.find_all("head")

embed()


"""

for head in headers:
    text = head.get_text()
    new_text = re.sub('H.llo', 'Hei', text)
    print(new_text)

"""
