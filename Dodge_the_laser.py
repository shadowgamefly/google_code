import math
# A Beatty sequnece
# A(n) = n * m + n(n + 1)/2 - m(m+1)/2 - A(m)
# m = floor((sqrt(2) - 1) * n)


def answer(str_n):
    n = int(str_n)
    return str(int(A(n)))

def m_val(n):
    return math.floor((math.sqrt(2) - 1) * n)

def A(n):
    if n < 2:
        return n
    else :
        m = m_val(n)
        return n * m + n * (n + 1) / 2 - m * (m + 1) / 2 - A(m)

print(answer('5'))
print(len('4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727'))
