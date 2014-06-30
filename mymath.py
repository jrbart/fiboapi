#!/usr/env python2

class RangeError(Exception):
    pass

class InputError(Exception):
    pass

def fibo(n):
    if n < 0:
        raise RangeError

    result = [0]
    a, b = 0, 1
    for i in range(n-1):
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    pass
