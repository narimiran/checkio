def berserk_rook(berserker, enemies):
    me = (ord(berserker[0])-96, int(berserker[1]))
    them = {(ord(enemy[0])-96, int(enemy[1])) for enemy in enemies}
    max_path = 0
    stack = [(me, set())]

    while stack:
        current, path = stack.pop()
        max_path = max(max_path, len(path))
        neighbours = find_closest(current, them-path)
        for neighbour in neighbours:
            stack.append((neighbour, path | {neighbour}))
    return max_path


def find_closest(me, them):
    up    = [rook for rook in them if rook[0] == me[0] and rook[1] > me[1]]
    down  = [rook for rook in them if rook[0] == me[0] and rook[1] < me[1]]
    right = [rook for rook in them if rook[0] > me[0] and rook[1] == me[1]]
    left  = [rook for rook in them if rook[0] < me[0] and rook[1] == me[1]]

    neigbours = []
    if up:    neigbours.append(min(up))
    if down:  neigbours.append(max(down))
    if right: neigbours.append(min(right))
    if left:  neigbours.append(max(left))
    return neigbours


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5, "one path"
    assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6, "several paths"
    assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4, "Don't jump through"