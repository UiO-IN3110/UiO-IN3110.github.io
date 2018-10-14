"""
Regular Expression can be used to do primitive search and substitutions.

.   any char
"""
import re

string = """
Man:        Well, what've you got?
Waitress:   Well, there's egg and bacon; egg sausage and bacon; egg and spam;
            egg bacon and spam; egg bacon sausage and spam; spam bacon sausage
            and spam; spam egg spam spam bacon and spam; spam sausage spam spam
            bacon spam tomato and spam;
Vikings:    Spam spam spam spam...
Waitress:   ...spam spam spam egg and spam; spam spam spam spam spam spam baked
            beans spam spam spam...
"""

print(re.sub("s.am", "ham", string))
