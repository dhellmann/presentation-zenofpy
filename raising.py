def f(n):
    if not isinstance(n, int):
        raise TypeError('n should be an int')
    if n > 0:
        return n * f(n-1)
    return 1

print f('5')