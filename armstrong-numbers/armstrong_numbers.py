def is_armstrong(number):
    digits = str(number)
    return number == sum(int(digit) ** len(digits) for digit in digits)
