def count_bits(n):
    count = 0
    while n >= 1:

        if (n % 2) == 1:
            count += 1
        n //= 2
    return count