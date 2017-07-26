from itertools import *
h = 0
w = 0
output_list = []


def answer(g):
    global h, w, output_list
    h = len(g) + 1
    w = len(g[0]) + 1
    pos_col = pow(2, h)
    init_list()
    count = [[0 for x in range(pos_col)] for y in range(w)]
    count[0] = [1 for x in range(pos_col)]
    for i in range(1, w):
        result = int(''.join([ "%d"%g[x][i - 1] for x in range(h - 1)]), 2)
        for j in range(pos_col):
            for col in output_list[result][j]:
                count[i][col] += count[i-1][j]
    return sum([count[w - 1][x] for x in range(pos_col)])

    # print(output_
def match(a, b):
    ret = [0 for x in range(h - 1)]
    for i in range(h - 1):
        if a[i] + a[i + 1] + b[i] + b[i + 1] == 1 :
            ret[i] = 1
    return ret


def init_list():
    global output_list
    pos_col = pow(2, h)
    pos_res = pow(2, h - 1)
    output_list = [[[] for x in range(pos_col)] for y in range(pos_res)]
    for a in list(product(range(2), repeat=h)):
        a = list(a)
        for b in list(product(range(2), repeat=h)):
            b = list(b)
            ret = match(a, b)
            a_val = int(''.join([ "%d"%x for x in a]), 2)
            ret_val = int(''.join([ "%d"%x for x in ret]), 2)
            output_list[ret_val][a_val].append(int(''.join([ "%d"%x for x in b]), 2))

print(answer([
[True, True, False, True, False, True, False, True, True, False],
                        [True, True, False, False, False, False, True, True, True, False],
                        [True, True, False, False, False, False, False, False, False, True],
                        [False, True, False, False, False, False, True, True, False, False],
                        [True, True, False, True, False, True, False, True, True, False],
                                                [True, True, False, False, False, False, True, True, True, False],
                                                [True, True, False, False, False, False, False, False, False, True],
                                                [False, True, False, False, False, False, True, True, False, False]
                      ]))
