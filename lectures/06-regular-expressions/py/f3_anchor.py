"""
Returning to the first example.
"""

import re

source_text = """
The target word is apple.

But to make it hard, I will throw in a pineapple

applemost.
"""

substituted_text = re.sub(r"\Bapple\b", "orange", source_text)
print(substituted_text)
