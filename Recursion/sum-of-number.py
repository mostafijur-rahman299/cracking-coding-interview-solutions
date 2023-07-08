def sum_of_digits(number):
    if len(str(number)) == 1:
        return number
    return sum_of_digits(number % 10) + sum_of_digits(number // 10)

sum_of_digits(550125)
