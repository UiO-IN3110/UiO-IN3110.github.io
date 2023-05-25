"""
Validate MAC addresses.
"""
import re


def is_valid_mac(addresses):
    """
    Validate that a list of strings are formatted as a valid MAC address.

    Example:
        >>> addresses = [
        ...     "af:04:52:FF:bc:5f",    # correct
        ...     "af:04:52:FF:bc:5f:99", # too long
        ...     "af:04:52:FF:bc",       # too short
        ...     "Pf:04:52:ZF:bc:5q",    # contains invalid chars
        ... ]
        >>> print(is_valid_mac(addresses))
        [True, False, False, False]
    """
    char = r"[0-9a-fA-F]"
    regex = ":".join([char * 2] * 6)
    regex = "^" + regex + "$"
    matches = [re.findall(regex, address) for address in addresses]
    matches = [match != [] for match in matches]
    return matches


if __name__ == "__main__":
    import doctest

    doctest.testmod()
