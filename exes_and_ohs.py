def xo(s):
    a = 0
    b = 0
    s = s.lower()
    for i in s:
        if i == 'o':
            a += 1
        if i == 'x':
            b += 1
    return a == b
