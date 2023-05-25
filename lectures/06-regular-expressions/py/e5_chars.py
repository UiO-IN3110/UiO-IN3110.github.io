"""
Find the numbers
"""

import re

search_text = "The bar is open between 18:04 and 02:00 every friday."
regex = r"[0-9]"
search_results = re.findall(regex, search_text)
print(search_results)
