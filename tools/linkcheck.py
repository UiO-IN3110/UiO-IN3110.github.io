import sys
from bs4 import BeautifulSoup
import requests
import requests_cache

requests_cache.install_cache()


def check_link(url):
    r = requests.get(url)
    if r.status_code == 200:
        sys.stdout.write(".")
        sys.stdout.flush()
    else:
        print(r.status_code, url)


def check_links(*paths):
    for path in paths:
        print(f"Checking {path}", end="")
        count = 0
        with open(path) as f:
            page = BeautifulSoup(f.read(), "html5lib")
            for a in page.find_all("a"):
                url = a.get("href")
                if url and not url.startswith("mailto:"):
                    check_link(url)
        print()


if __name__ == "__main__":
    check_links(*(sys.argv[1:] or ["index.html"]))
