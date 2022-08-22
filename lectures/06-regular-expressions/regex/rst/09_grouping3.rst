Groupings 3
===========

Groups can also be used as back reference `(string)` using slash numbers `\1`::

    r"(A) B \1"     ->  "A B A"

Multiple groups can be referenced at once::

    r"(A) (B) (C) \3 \2 \1"     ->      "A B C C B A"

Adding `?:` prefix marker means non-capturing::

    r"(?:A) (B) \1" -> "A B B"
