def solution(x, y):
    xor_result = 0

    # Perform XOR operation on all elements in list x
    for num in x:
        xor_result ^= num

    # Perform XOR operation on all elements in list y
    for num in y:
        xor_result ^= num

    return xor_result
