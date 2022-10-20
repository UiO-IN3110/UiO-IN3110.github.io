# Test with no params
import pytest
from bs4 import BeautifulSoup
from requesting_urls import get_html


@pytest.mark.parametrize(
    "url, expected",
    [
        ("https://en.wikipedia.org/wiki/Studio_Ghibli", "Studio Ghibli"),
        ("https://en.wikipedia.org/wiki/Star_Wars", "Star Wars"),
        ("https://en.wikipedia.org/wiki/Dungeons_%26_Dragons", "Dungeons"),
    ],
)
def test_get_html_no_params(url, expected):
    html = get_html(url)
    assert isinstance(html, str)
    assert "<!DOCTYPE" in html
    assert "<html" in html
    assert expected in html


# Test with params
@pytest.mark.parametrize(
    "params, expected",
    [
        ({"title": "Main_Page"}, "<title>Wikipedia"),
        ({"title": "Hurricane_Gonzalo", "oldid": "983056166"}, "<title>Hurricane"),
    ],
)
def test_get_html_params(params, expected):
    url = "https://en.wikipedia.org/w/index.php"

    html = get_html(url, params=params)
    assert expected in html


def test_get_html_output(tmpdir):
    url = "https://uio-in3110.github.io"
    dest = tmpdir.join("output.txt")
    html = get_html(url, output=str(dest))
    assert dest.exists()  # assert output file was created

    with dest.open() as f:
        written_output = f.read()

    first_line, rest = written_output.split("\n", 1)
    assert url in first_line
    assert "<html" in rest
    assert "Higher Level Programming" in rest
    assert rest.strip().endswith("</html>")
