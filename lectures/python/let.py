# Local scopes mimicking let ... end in Juli
# Inspired by https://stackoverflow.com/questions/61371134/python-let-with-local-scopes-debug-printing-and-temporary-variables
from contextlib import contextmanager
from inspect import currentframe, getouterframes


@contextmanager
def let(**bindings):
    # 2 because first frame in `contextmanager` is the decorator
    frame = getouterframes(currentframe(), 2)[-1][0]
    locals_ = frame.f_locals
    old_vars = set(locals_)
    original = {var: locals_.get(var) for var in bindings}
    locals_.update(bindings)
    yield
    locals_.update(original)
    # Cleanup
    for var in set(bindings).difference(old_vars):
        del locals_[var]


# --------------------------------------------------------------------
if __name__ == "__main__":
    import importlib

    b = 3
    with let(np=importlib.import_module("numpy"), x=2, y=4, b=5):
        ans = np.zeros((x, y))  # noqa

    print(ans)
    print("b is as before let", b)
    try:
        print(np, x, y)
    except NameError:
        print("np x y not visible in this scope")
