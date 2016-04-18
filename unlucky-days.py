from datetime import date

def checkio(year):
    return sum(date(year, month, 13).isoweekday() == 5 for month in range(1, 13))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
