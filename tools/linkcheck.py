from bs4 import BeautifulSoup
import requests
import requests_cache

requests_cache.install_cache()


def check_link(url):
    r = requests.get(url)
    print(r.status_code, url)


def check_links(*paths):
    for path in paths:
        print(f"Checking {path}")
        with open(path) as f:
            page = BeautifulSoup(f.read(), "html5lib")
            for a in page.find_all("a"):
                url = a.get("href")
                if url:
                    check_link(url)


if __name__ == "__main__":
    check_links("index.html")
