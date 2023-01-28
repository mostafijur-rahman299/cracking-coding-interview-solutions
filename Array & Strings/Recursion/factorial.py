
def factorial_number(n):
    if n == 1:
        return 1
    return n * factorial_number(n - 1)

factorial_number(5)
