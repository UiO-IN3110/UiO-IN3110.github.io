"""
Lines starts with a '^' anchor.
"""

import re

search_text = "apple 1, apple 2, and apple 3"

regex = r"$apple \d"

search_results = re.findall(regex, search_text)

print(search_results)
