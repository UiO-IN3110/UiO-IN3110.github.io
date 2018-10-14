"""
Validate IP addresses.

+   one or more
*   zero or more
"""
import re


def is_valid_ip(addresses):
    """
    Validate that a list of strings are formatted as valid IP addresses.

    Example:
        >>> addresses = [
        ...     "127.0.0.1",
        ...     "127.0.0.0.1",
        ...     "127.000.000.001",
        ...     "1127.000.000.001",
        ...     "256.000.000.001",
        ... ]
        >>> print(is_valid_ip(addresses))
        [True, False, True, False, False]
    """
    regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])(?:\.\1){3}$"
    matches = [re.findall(regex, address) for address in addresses]
    matches = [match != [] for match in matches]
    return matches


if __name__ == "__main__":
    import doctest
    doctest.testmod()
