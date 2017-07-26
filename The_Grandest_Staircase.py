import math
def answer(n):
    # result[x][y] specify number of possible layout within x blocks and y steps
    result = [[0 for x in range(n + 1)] for y in range(n + 1)]

    result[1][1] = 1

    for h in range(1, n + 1):
        result[h][1] = 1

    for d in range(2, n + 1):
        for h in range(2, int(math.sqrt(d * 2)) + 1):
            diff = 1
            while diff * h < d:
                result[d][h] += result[d - diff * h][h - 1]
                diff += 1

    return sum(result[n]) - 1

print(answer(200))
