def checkio(number):
    factors = []
    for divisor in "98765432":
        while not number % int(divisor):
            factors.append(divisor)
            number //= int(divisor)
    return int(''.join(reversed(factors))) if number == 1 else 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
