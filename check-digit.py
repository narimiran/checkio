def checkio(data):
    rev = (a for a in reversed(data) if a.isalnum())
    total = 0
    for i, val in enumerate(rev):
        v = ord(val) - 48
        total += [sum(divmod(v*2, 10)), v][i%2]
    final = str(-total % 10)
    return [final, total]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, solved!")