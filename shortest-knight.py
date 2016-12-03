from collections import deque

def checkio(cells):
    first, second = cells.split('-')
    start = (ord(first[0])-96, int(first[1]))
    finish = (ord(second[0])-96, int(second[1]))
    knight = [(-1, -2), (-1, 2), (1, -2), (1, 2),
              (-2, -1), (-2, 1), (2, -1), (2, 1)]
    seen = set()
    que = deque([(start, 0)])

    while que:
        (x, y), moves = que.popleft()
        moves += 1
        seen |= {(x, y)}
        for dx, dy in knight:
            nx, ny = (x + dx, y + dy)
            if 0 < nx <= 8 and 0 < ny <= 8 and (nx, ny) not in seen:
                if (nx, ny) == finish:
                    return moves
                que.append(((nx, ny), moves))


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"