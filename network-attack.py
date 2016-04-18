def capture(matrix):
    infected = {0}
    time = 0
    while len(infected) < len(matrix):
        time += 1
        infected_this_turn = set()
        already_visited = set()
        for inf in infected:
            for i, row in enumerate(matrix):
                if i in infected or i in already_visited:
                    continue
                if row[inf]:
                    row[i] -= 1
                    already_visited.add(i)
                    if row[i] == 0:
                        infected_this_turn.add(i)
        infected |= infected_this_turn
    return time


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
