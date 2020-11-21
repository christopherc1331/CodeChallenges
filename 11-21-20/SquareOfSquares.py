import math


def is_square(n):
    return False if n < 0 else True if math.sqrt(n).is_integer() else False
