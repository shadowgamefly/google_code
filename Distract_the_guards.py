def match(a, b):
    if a == b :
        return False
    s = a + b;
    if s % 4 != 0:
        return True
    else :
        appeard = set()
        while a not in appeard:
            appeard.add(a)
            appeard.add(b)
            if a == b :
                return False
            elif a > b :
                a -= b
                b *= 2
            else :
                b -= a
                a *= 2
        return True

def answer(banana_list):
    l = len(banana_list)
    chart = [set([j for j in range(l) if match(banana_list[i], banana_list[j])]) for i in range(l)]
    used = set()
    count = 0
    while True:
        index = -1
        num = float("inf")
        for i in range(l):
            cur_num = len(chart[i])
            if cur_num < num and cur_num > 0:
                index = i
                num = cur_num
        if index == -1 :
            break
        to_remove = chart[index].pop()
        chart[index] = set()
        chart[to_remove] = set()
        for s in chart:
            s.discard(index)
            s.discard(to_remove)
        count += 2
    return l - count

print(answer([1, 7, 3, 21, 13, 9]))
