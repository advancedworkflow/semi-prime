from functools import wraps
import time
from math import gcd
import random


def rabinMiller(n):
    try:
        if n == 2:
            return True

        if n % 2 == 0:
            return False

        if n in [0, 1]:
            raise TypeError
        if n == 3:
            return True

        m = n - 1
        p = 0

        while m % 2 == 0:
            m = m // 2
            p += 1
        for i in range(5):

            a = random.randrange(2, n - 1)

            b = pow(a, m, n)
            if b != 1:
                j = 0
                while b != (n - 1):
                    if j == p - 1:
                        return False
                    else:
                        j = j + 1
                        b = (b ** 2) % n
        return True


    except TypeError:
        return f'error'





def f(x):
    return x * x + 1


def factor(n):
    if n not in [0, 1]:

        x, y, d = 2, 2, 1
        while d == 1:
            x = f(x) % n
            y = f(f(y)) % n
            d = gcd(x - y, n)
        return d
    else:
        return False


def sm(n):
    start_time = time.perf_counter()
    print(start_time)
    if factor(n):
        p = factor(n)
        q = int(n / p)
        if rabinMiller(q) == True:
            end_time = time.perf_counter()
            timer = start_time - end_time
            print(start_time)
            return [(p, q), timer]
        else:
            return 'le nombre n\'est pas semi premier'
    else:
        return 'nombre saisi est incorrect '



