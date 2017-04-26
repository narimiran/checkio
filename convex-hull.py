from collections import namedtuple

Point = namedtuple('Point', 'x y i')

def checkio(data):
    # https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain
    def not_right_turn(a, b, c):
        return (b.x - a.x)*(c.y - a.y) > (b.y - a.y)*(c.x - a.x)

    def half(points):
        hull = []
        for point in points:
            while len(hull) > 1 and not_right_turn(hull[-2], hull[-1], point):
                hull.pop()
            hull.append(point)
        return [p.i for p in hull[:-1]]

    points = sorted(Point(x, y, i) for i, (x, y) in enumerate(data))
    return half(points) + half(reversed(points))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"
