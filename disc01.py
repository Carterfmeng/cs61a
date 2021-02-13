## if statements

##Boolean Operators

##Question 1.1
def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining

def handle_overflow(s1, s2):
    if s1 <= 30 and s2 <= 30:
        print("No overflow.")
    elif s1 > 30 and s2 > 30:
        print("No space left in either section")
    elif s1 <= 30:
        a = 30 - s1
        print("{a} spot left in Section 1 ")
    else:
        b = 30 - s2
        print("{b} spot left in Section 2")