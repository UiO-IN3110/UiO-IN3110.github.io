r"""
Lets make things more challenging.

.   any char
\w  word char       [a-zA-Z0-9]
\W  not word char   [^a-zA-Z0-9]
\d  digit char      [0-9]
"""
import re

string = """
Man:        Well, what've you got?
Waitress:   Well, there's egg and bacon; egg sausage and bacon; egg and sp?m;
            egg bacon and sp4m; egg bacon sausage and 5pam; spam bacon sausage
            and sham; Spam egg sham span bacon and SPAM; psam sausage slam scam
            bacon tram tomato and span;
Vikings:    Scam spem spat stam...
Waitress:   ...slam sapm span egg and cpam; zpam SPAN spam spam spam sp&m baked
            beans sp7m sp%m spAm...
"""
print(re.findall(r"sp.m", string))
