
# Fibonacci by recursions
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))


# Fibonacci by iteration
def fibonacci_number(number):
    a = 0
    b = 1
    for i in range(number):
        c = a + b
        a = b
        b = c
