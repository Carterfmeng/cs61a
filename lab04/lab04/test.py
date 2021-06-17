def a():
    return 100

def b():
    return 20

def c():
    return d()

def d():
    a()
    b()

t = c()

