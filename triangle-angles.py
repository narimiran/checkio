from math import acos, degrees

def checkio(a, b, c):
    a, b, c = sorted((a, b, c))
    if a + b <= c:
        return [0, 0, 0]
    alfa = round(degrees(acos((b**2 + c**2 - a**2) / (2*b*c))))
    beta = round(degrees(acos((c**2 + a**2 - b**2) / (2*c*a))))
    gama = 180 - alfa - beta
    return [alfa, beta, gama]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
