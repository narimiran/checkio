from itertools import combinations


def checkio(data):
    def difference(weight):
        return abs(balanced - weight)

    balanced = sum(data) / 2
    half_range = range(len(data)//2 + 1)
    sums = {sum(values) for n in half_range for values in combinations(data, n)}
    closest = min(sums, key=difference)
    return 2 * abs(balanced - closest)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
