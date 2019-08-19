"""
Partial case insensitive search.
"""

import re

search_text = "Hello, hello, hello, HELLO."

regex = "[Hh]ello"

search_results = re.findall(regex, search_text)
print(search_results)
