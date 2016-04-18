FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(n):
    r = [n//100, n%100//10, n%10]
    s = []

    if r[0] > 0:
        s.extend([FIRST_TEN[r[0]], HUNDRED])
    if r[1] > 1:
        s.append(OTHER_TENS[r[1]-2])
    if r[1] == 1:
        s.append(SECOND_TEN[r[2]])
        return ' '.join(s)
    if r[2] > 0:
        s.append(FIRST_TEN[r[2]])
    return ' '.join(s)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(42) == 'forty two', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
