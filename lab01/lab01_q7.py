def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"

    if n < 10:
        return False
    else:
        while (n // 10) != 0 :
            single = n % 10
            if single == 8:
                next_single = n // 10 % 10
                if (next_single == 8):
                    return True
                else:
                    n = n // 100
            else:
                n = n // 10
        return False
        

