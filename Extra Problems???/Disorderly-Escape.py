from math import factorial

def count_occurrences(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

def cycle_count(c, n):
    cc = factorial(n)
    for a, b in count_occurrences(c).items():
        cc //= (a ** b) * factorial(b)
    return cc

def cycle_partitions(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in cycle_partitions(n - i, i):
            yield [i] + p

def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(w, h, s):
    grid_count = 0
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):
            cpw_count = cycle_count(cpw, w)
            cph_count = cycle_count(cph, h)
            cpw_gcd_sum = sum([sum([greatest_common_divisor(i, j) for i in cpw]) for j in cph])
            grid_count += cpw_count * cph_count * (s ** cpw_gcd_sum)

    total_count = factorial(w) * factorial(h)
    return str(grid_count // total_count)
