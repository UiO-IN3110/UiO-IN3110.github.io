from functools import partial

from bs4 import BeautifulSoup


def _clean_annotated_html(original_clean, html):
    """Substitute inline Cython annotated output

    extracts body and style contents to avoid
    """
    html = original_clean(html)
    page = BeautifulSoup(html, "html.parser")
    chunks = []
    # could do this only once, but then clearing output and re-running would lose style.
    for style in page.find_all("style"):
        chunks.append(str(style))
    # add css to fix cython line padding in jupyter-book output
    chunks.append('<style type="text/css">.cython.line { padding: 0px; }</style>')
    chunks.append("".join(str(element) for element in page.find("body").contents))
    return "\n".join(chunks)


def load_ipython_extension(ip):
    cython_magics = ip.magics_manager.magics["cell"]["cython"].__self__
    original_clean = cython_magics.clean_annotated_html
    cython_magics.clean_annotated_html = partial(_clean_annotated_html, original_clean)
