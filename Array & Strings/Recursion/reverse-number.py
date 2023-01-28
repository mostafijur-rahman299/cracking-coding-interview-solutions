def rev(n, digits):
    if n % 10 == n: return n
    rem = n % 10
    return rem * (10 ** (digits-1)) + rev(n // 10, digits - 1)

print(rev(219893, 6))

