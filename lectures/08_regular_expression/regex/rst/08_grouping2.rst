Groupings 2
===========

Groups can include more than one string `(?:string1|string2)`.

Groups can be used to repeat strings. E.g.::

    r"(AB|CD)"     ->  "AB" or "CD"

    r"(?:AB|CD|EF)"  ->  "AB" or "CD" or "EF"

    r"(?:AB|CD)+"    ->  "AB" or "CD" or "ABAB" or "CDAB" or ..
