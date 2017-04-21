def checkio(required, operations):
    regions = []
    for idx, (left, right) in enumerate(operations, 1):
        for region in regions[:]:
            reg_l, reg_r = region
            if reg_l <= left <= reg_r or left <= reg_l <= right:
                left = min(reg_l, left)
                right = max(reg_r, right)
                regions.remove(region)
        regions.append((left, right))
        if sum((r - l + 1) for (l, r) in regions) >= required:
            return idx
    return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
