from itertools import combinations
from math import acos, hypot, pi


left = lambda a, b: min(a[0], b[0])
area = lambda r: r**2 * pi


def distance(a, b):
    x1, y1, _ = a
    x2, y2, _ = b
    return hypot(x1-x2, y1-y2)


def intersection_area(a, b, d):
    r1, r2 = a[-1], b[-1]
    if r1 + r2 <= d:
        return 0
    if r1 > d + r2:
        return area(r2)

    # http://mathworld.wolfram.com/Circle-CircleIntersection.html
    s = (2 * d * r1)**2 - (d**2 + r1**2 - r2**2)**2
    d1 = (d**2 + r1**2 - r2**2) / (2 * d * r1)
    d2 = (d**2 + r2**2 - r1**2) / (2 * d * r2)
    return r1**2 * acos(d1) + r2**2 * acos(d2) - 0.5 * s**0.5


def checkio(data):
    holes = [list(hole) for hole in data]
    while True:
        pairs = sorted((distance(a, b), left(a, b), a, b)
                       for a, b in combinations(holes, 2))
        for d, _, a, b in pairs:
            smaller, bigger = sorted((a, b), key=lambda x: x[-1])
            A1, A2 = area(bigger[-1]), area(smaller[-1])
            A_inter = intersection_area(bigger, smaller, d)
            if A_inter >= 0.55 * A2 and A1 >= 1.2 * A2:
                bigger[-1] = ((A1 + A2) / pi)**0.5
                holes.remove(smaller)
                break
        else:
            break
    return [(x, y, round(r, 2)) for (x, y, r) in holes]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
    assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)]
    assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)]
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]
