from itertools import combinations, permutations


def place_queens(placed):
    for (c1, r1), (c2, r2) in combinations(placed, 2):
        if c1 == c2 or r1 == r2 or abs(ord(c1)-ord(c2)) == abs(int(r1)-int(r2)):
            return set()

    cols = list("abcdefgh")
    rows = list("12345678")

    for c, r in placed:
        cols.remove(c)
        rows.remove(r)

    for perm in permutations(rows, len(rows)):
        occupied = placed.copy()
        candidates = [cols[i]+r for i, r in enumerate(perm)]

        for queen in candidates:
            if all(abs(ord(queen[0])-ord(col)) != abs(int(queen[1])-int(row))
                   for (col, row) in occupied):
                occupied.add(queen)
            else:
                break
        else:
            return occupied
    return set()


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import combinations
    COLS = "abcdefgh"
    ROWS = "12345678"

    THREATS = {c + r: set(
        [c + ROWS[k] for k in range(8)] +
        [COLS[k] + r for k in range(8)] +
        [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8] +
        [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
               for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}

    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example"
    assert checker(place_queens, {"b2", "c4", "d6", "e8", "a7", "g5"}, False), "2nd Example"

