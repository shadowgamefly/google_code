def answer(h, q):
    for val in q:
        num = pow(2, h) - 1
        top = -1
        prev_cut = False
        cut = 0
        for d in range(h):
            if num == val :
                if prev_cut == True:
                    return top + cut - num
                else :
                    return top + cut
            else :
                top = num
                if val < (num + 1) / 2:
                    num = (num - 1) / 2
                    prev_cut = False
                else:
                    val = val - (num - 1) / 2
                    cut = cut + (num - 1) / 2
                    num = (num - 1) / 2
                    prev_cut = True

print(answer(5, [19, 2, 3]))
