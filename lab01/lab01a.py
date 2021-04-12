# Q1：
def xk(c, d):
    """
    >>> xk(10, 10)
    23
    >>> xk(10, 6)
    23
    >>> xk(4, 6)
    6
    >>> xk(0, 0)
    25
    """

    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25


def how_big(x):
    """
    >>> how_big(7)
    'big'
    >>> how_big(12)
    huge
    >>> how_big(1)
    small
    >>> how_big(-1)
    nothin
    """
    if x > 10:
       print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothin")

# >>> n = 3
# >>> while n >= 0:
# ...     n -= 1
# ...     print(n)
# ______

# 2
# 1
# 0
# -1

# >>> positive = 28
# >>> while positive:
# ...    print("positive?")
# ...    positive -= 3
# ______

# positive?
# positive?
# positive?
# ……

# >>> positive = -9  -6 -3 0 3
# >>> negative = -12  -9 -6 -3 0
# >>> while negative:
# ...    if positive:
# ...        print(negative)
# ...    positive += 3
# ...    negative += 3
# -12
# -9
# -6

# Q2:



