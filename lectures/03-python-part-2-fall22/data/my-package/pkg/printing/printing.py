from functools import partial


GREEN = '\033[1;37;32m%s\033[0m'
RED = '\033[1;37;31m%s\033[0m'
BLUE = '\033[1;37;34m%s\033[0m'


def print_color(color, string):
    '''Print with color'''
    print(color % string)
    # NOTE: this is here just to have something to test
    return color


print_red = partial(print_color, RED)
print_green = partial(print_color, GREEN)
print_blue = partial(print_color, BLUE)

# --------------------------------------------------------------------

if __name__ == '__main__':
    print_red('FAILS!')
    print_green('WORKS!')
