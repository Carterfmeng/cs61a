def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    digit = 0
    sum_digit = 0
    if y >= 10:
        while y // 10 != 0:
            digit = y % 10
            sum_digit = sum_digit + digit
            y = y // 10
        sum_digit = sum_digit + y
        return sum_digit
    else:
        return y




