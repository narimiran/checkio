def checkio(number):
    a = str(number)
    total = 1
    for digit in a:
        if int(digit):
            total *= int(digit)
    return total


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
