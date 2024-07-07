def solution(x, y):
    xor_result = 0
    for num in x:
        xor_result ^= num
    for num in y:
        xor_result ^= num
    return xor_result
