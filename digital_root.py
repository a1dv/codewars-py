def digital_root(n):
    a = 0
    for i in range(len(str(n))):
        a += n % 10
        n //= 10
    if len(str(a)) > 1:
        return digital_root(a)
    return a
