def answer(l):
    s = sum(l)
    l.sort()
    one, two, three = [], [], []
    for n in l:
        if n % 3 == 1:
            one.append(n)
        elif n % 3 == 2:
            two.append(n)
        else :
            three.append(n)
    if s % 3 == 1:
        if len(one) > 0 :
            l.remove(one[0])
        elif len(two) > 1:
            l.remove(two[0])
            l.remove(two[1])
        else :
            return 0
    elif s % 3 == 2:
        if len(two) > 0:
            l.remove(two[0])
        elif len(one) > 1:
            l.remove(one[0])
            l.remove(one[1])

    retval = 0

    for i in range(len(l)):
        retval = retval * 10 + l[len(l) - 1 - i]

    return retval

print(answer([2,2]))
