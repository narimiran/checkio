from math import atanh, asin, sqrt, pi

def checkio(height, width):
    a, c = width/2, height/2
    if a > c:
        e = sqrt(1 - (c**2/a**2))
        area = 2 * pi * a**2 * (1 + atanh(e) * ((1 - e**2)/e))
    else:
        e = sqrt(1 - (a**2/c**2))
        if e == 0:
            area = 4 * pi * a**2
        else:
            area = 2 * pi * a**2 * (1 + asin(e) * (c / (a*e)))
    volume = round((4/3) * pi * a**2 * c, 2)
    return [volume, round(area, 2)]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"