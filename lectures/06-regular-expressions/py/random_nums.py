import numpy as np


def random_string(n=10):
    """String of words and numbers"""
    randoms = (random_word, random_real, random_int)
    return " ".join([np.random.choice(randoms, 1)[0]() for _ in range(n)])


def random_word(l=8):
    """Random letters of length l in [a-zA-Z]"""
    letters = tuple(map(chr, np.r_[np.arange(65, 91), np.arange(97, 123)]))
    return "".join(np.random.choice(letters, l))


def random_real():
    """As string"""
    n = np.random.randn()
    formats = ("%g", "%.4E", "%.8e", "%.2f")
    (fmt,) = np.random.choice(formats, 1)
    return fmt % n


def random_int():
    """As string"""
    return str(np.random.randint(10_000_000))
