from itertools import permutations as perm


def checkio(chips):
    try:
        return max(sum((a, b, c, d, e, f))
                   for bb, cc, dd, ee, ff in perm(chips[1:])
                   for al, a, ar in perm(chips[0])
                   for bl, b, br in perm(bb) if ar == bl
                   for cl, c, cr in perm(cc) if br == cl
                   for dl, d, dr in perm(dd) if cr == dl
                   for el, e, er in perm(ee) if dr == el
                   for fl, f, fr in perm(ff) if er == fl and fr == al
                  )
    except ValueError:
        return 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"
