Groupings 1
===========

Multiple characters can be grouped together using `(?:string)`.

Groups can be used to repeat strings. E.g.::

    r"(?:ABC)?"  ->  "" or "ABC"
    r"(?:ABC)*"  ->  "" or "ABC" or "ABCABC" or ..
    r"(?:ABC)+"  ->  "ABC" or "ABCABC" or "ABCABCABC" or ..

Compared to character classes::

    r"[ABC]?"   ->  "" or "A" or "B" or "C"
    r"[ABC]*"   ->  "" or "A" or "B" or "C" or "AA" or "AB" or ..
    r"[ABC]+"   ->  "A" or "B" or "C" or "AA" or "AB" or "AC" or ..
