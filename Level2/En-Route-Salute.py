def solution(s):
    salute_count = 0
    employees_walking_right = 0

    for char in s:
        if char == '>':
            employees_walking_right += 1
        elif char == '<':
            salute_count += employees_walking_right

    return salute_count * 2
