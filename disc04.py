# 1.1
def sum_of_factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n) + sum_of_factorial(n - 1)

#theta(n2)

# 1.2
def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

#theta(2n) / theta(1.6n) 黄金比例

#1.3 
def fib_iter(n):
    prev, curr, i = 0, 1, 0
    while i < n:
        prev, curr = curr, prev + curr
        i += 1
    return prev
# theta(n)

#1.4 
def bonk(n):
    total = 0
    while n >= 2:
        total += n
        n = n / 2
    return total

#theta(logn)

#1.5 
def mod_7(n):
    if n % 7 == 0:
        return 0
    else:
        return 1 + mod_7(n - 1)
#theta(n)

#1.6 
def bar(n):
    if n % 2 == 1:
        return n + 1
    return n

def foo(n):
    if n < 1:
        return 2
    if n % 2 == 0:
        return foo(n - 1) + foo(n - 2)
    else:
        return 1 + foo(n - 2)

# What is the order of growth of foo(bar(n))?

#theta(n2)


#2.3 Write a function that updates and prints a value x based on input functions.
def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def helper(func):
        nonlocal n
        n = func(n)
        print(n)
        return helper
    return helper

#3.3 Reverse a list in place, i.e. mutate the given list itself, instead of returning a new list.
def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    for i in range(len(lst)-1):
        lst.insert(i,lst[-1])
        lst.pop(-1)
    return

    # for i in range(len(lst) // 2):
    #   lst[i], lst[-i - 1] = lst[-i - 1], lst[i]