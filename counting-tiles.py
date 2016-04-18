from math import sqrt


def checkio(radius):
    solid = 0
    partial = 0

    for x in range(int(radius)+1):
        for y in range(int(radius)+1):
            if sqrt((x+1)**2 + (y+1)**2) < radius:
                solid += 1
            elif sqrt(x**2 + y**2) < radius:
                partial += 1
    return [4*solid, 4*partial]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
