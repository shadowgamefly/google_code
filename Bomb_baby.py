def answer(M, F):
    M = long(M)
    F = long(F)
    count = 0
    while M > 0 and F > 0 :
        if M == 1 :
            return count + F - 1
        if F == 1 :
            return count + M - 1
        if M > F:
            count += M // F
            M = M % F
        else :
            count += F // M
            F = F % M

    return "impossible"

print(answer(4, 7))
