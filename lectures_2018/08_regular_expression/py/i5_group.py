"""
Non-capturing groups is encurrage to separete grouping from capturing.
"""

import re

source_text = "mohahahahahahe"

regex_in = r"(\w*?)(?:ha)*(he)"     # Check this
regex_out = r"\2\1"

#print(re.findall(regex_in, source_text))
substituted_text = re.sub(regex_in, regex_out, source_text)
print(substituted_text)
