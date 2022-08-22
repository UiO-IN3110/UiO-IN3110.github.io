"""
Caveat: When is a newline an actual new line?

Flagging with `re.M`/`re.MULTILINE`.
"""
import re

search_text = """blue berries
apples, oranges, and
pineapples.
"""

regex = r"^\w\w\w\w"

search_results = re.findall(regex, search_text, flags=re.MULTILINE)
print(search_results)
