def is_armstrong(number):
    digits = []
    tmp = number
    while tmp > 0:
        digits.append(tmp % 10)
        tmp //= 10
    return number == sum(digit ** len(digits) for digit in digits)
