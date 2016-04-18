from copy import deepcopy


def checkio(grid):
    stack = [grid]
    while stack:
        board = stack.pop()
        new_board = populate_board(board)
        if new_board == 'complete':
            return board
        for b in new_board:
            stack.append(b)


def populate_board(grid):
    free_cells = {}
    for row in range(9):
        for col in range(9):
            candidates = set(range(1, 10))
            if grid[row][col] == 0:
                same_square = {grid[row//3*3+i][col//3*3+j]
                               for i in range(3) for j in range(3)}
                same_row = set(grid[row])
                same_col = {grid[i][col] for i in range(9)}
                candidates -= same_square | same_row | same_col

                if len(candidates) == 1:
                    grid[row][col] = candidates.pop()
                    return populate_board(grid)
                elif not candidates:
                    return ''
                else:
                    free_cells[(row, col)] = candidates
    if not free_cells:
        return 'complete'

    row, col = min(free_cells, key=lambda k: len(free_cells[k]))

    new_board = []
    for candidate in free_cells[(row, col)]:
        new_grid = deepcopy(grid)
        new_grid[row][col] = candidate
        new_board.append(new_grid)
    return new_board


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 7, 1, 6, 8, 4, 0, 0, 0],
                    [0, 4, 9, 7, 0, 0, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 0, 0, 0, 0, 5, 0, 4],
                    [0, 0, 0, 3, 0, 7, 0, 0, 0],
                    [2, 0, 3, 0, 0, 0, 0, 9, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [0, 0, 0, 0, 0, 3, 7, 2, 0],
                    [0, 0, 0, 4, 9, 8, 6, 1, 0]]) == [[3, 7, 1, 6, 8, 4, 9, 5, 2],
                                                      [8, 4, 9, 7, 2, 5, 3, 6, 1],
                                                      [5, 6, 2, 9, 3, 1, 4, 7, 8],
                                                      [6, 8, 7, 2, 1, 9, 5, 3, 4],
                                                      [9, 1, 4, 3, 5, 7, 2, 8, 6],
                                                      [2, 5, 3, 8, 4, 6, 1, 9, 7],
                                                      [1, 3, 6, 5, 7, 2, 8, 4, 9],
                                                      [4, 9, 8, 1, 6, 3, 7, 2, 5],
                                                      [7, 2, 5, 4, 9, 8, 6, 1, 3]], "first"
    assert checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4],
                    [0, 0, 1, 0, 3, 0, 5, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 5, 9, 7, 2, 6, 4, 0],
                    [0, 0, 0, 6, 0, 1, 0, 0, 0],
                    [0, 2, 6, 3, 8, 5, 9, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3, 0, 5, 0, 2, 0, 0],
                    [8, 0, 0, 4, 9, 7, 0, 0, 6]]) == [[5, 6, 8, 7, 1, 9, 3, 2, 4],
                                                      [9, 7, 1, 2, 3, 4, 5, 6, 8],
                                                      [2, 3, 4, 5, 6, 8, 7, 9, 1],
                                                      [1, 8, 5, 9, 7, 2, 6, 4, 3],
                                                      [3, 9, 7, 6, 4, 1, 8, 5, 2],
                                                      [4, 2, 6, 3, 8, 5, 9, 1, 7],
                                                      [6, 1, 9, 8, 2, 3, 4, 7, 5],
                                                      [7, 4, 3, 1, 5, 6, 2, 8, 9],
                                                      [8, 5, 2, 4, 9, 7, 1, 3, 6]], "second"
    print('Local tests done')

    a = checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4],
      [0, 0, 1, 0, 3, 0, 5, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 8, 5, 9, 7, 2, 6, 4, 0],
      [0, 0, 0, 6, 0, 1, 0, 0, 0],
      [0, 2, 6, 3, 8, 5, 9, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 3, 0, 5, 0, 2, 0, 0],
      [8, 0, 0, 4, 9, 7, 0, 0, 6]])

    for row in a:
        print(row)
