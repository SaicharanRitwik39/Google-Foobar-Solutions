from decimal import *

def sum_floor(a, n):
    if n == 0:
        return 0
    np = int((a - 1) * n)
    return n * np + n * (n + 1) / 2 - np * (np + 1) / 2 - sum_floor(a, np)

def solution(s):
    getcontext().prec = 101
    sqrt2 = Decimal(2).sqrt()
    return str(int(sum_floor(sqrt2, int(s))))
