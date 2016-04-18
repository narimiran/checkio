def safe_pawns(pawns):
    safe_ones = 0
    for col, row in pawns:
        defender_row = str(int(row)-1)
        left_defender = chr(ord(col)-1) + defender_row
        right_defender = chr(ord(col)+1) + defender_row

        if left_defender in pawns or right_defender in pawns:
            safe_ones += 1

    return safe_ones


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
