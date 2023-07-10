def solution(l):
    trips = 0
    doubs = [0]*len(l)

    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                doubs[i] += 1
                trips += doubs[j]
    return trips
