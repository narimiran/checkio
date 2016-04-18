from fractions import gcd


def divide_pie(groups):
    total = sum(abs(i) for i in groups)
    remaining = [total, total]

    for drones in groups:
        common = gcd(drones, total)
        current = [drones//common, total//common]

        if current[0] > 0:
            remaining[0] = remaining[0]*current[1] - current[0]*remaining[1]
            remaining[1] *= current[1]

        if current[0] < 0:
            remaining[0] *= current[0] + current[1]
            remaining[1] *= current[1]

        common = gcd(int(remaining[0]), int(remaining[1]))
        remaining[0] //= common
        remaining[1] //= common

    return tuple(remaining)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
