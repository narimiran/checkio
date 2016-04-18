def checkio(opacity):
    a, b = 1, 1
    age = 0
    while opacity != 10000:
        age += 1
        if age == b:
            opacity += b
            a, b = b, a+b
        else:
            opacity -= 1
    return age


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
