from copy import deepcopy
from itertools import chain, product


def is_possible(board):
    def check_line(line):
        return sum(line) == target if all(line) else sum(line) < target
    def check_diag(board):
        values = [board[i][i] for i in range(n)]
        return sum(values) == target if all(values) else sum(values) < target

    n = len(board)
    target = 0.5 * n * (n**2 + 1)

    return (all(check_line(row) for row in board) and
            all(check_line(col) for col in zip(*board)) and
            check_diag(board) and
            check_diag(list(zip(*board[::-1]))))


def checkio(data):
    n = len(data)
    nr = range(n)
    candidates = set(range(n**2 + 1)) - set(chain.from_iterable(data))

    stack = [(deepcopy(data), candidates)]
    while stack:
        board, unused = stack.pop()
        if not unused:
            return board

        r, c = next((r, c) for r, c in product(nr, repeat=2) if not board[r][c])
        for candidate in unused:
            board[r][c] = candidate
            if is_possible(board):
                stack.append((deepcopy(board), unused-{candidate}))



if __name__ == '__main__':
    #This part is using only for self-testing.
    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        #check sizes
        N = len(result)
        if len(result) == N:
            for r in result:
                if len(r) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
        #check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for r in result:
            if sum(r) != line_sum:
                print(MS_ERROR)
                return False
        for c in zip(*result):
            if sum(c) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        #check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
        #check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True


    assert check_solution(checkio,
                          [[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 0]]), "1st example"

    assert check_solution(checkio,
                          [[0, 0, 0],
                           [0, 5, 0],
                           [0, 0, 0]]), "2nd example"

    assert check_solution(checkio,
                          [[1, 15, 14, 4],
                           [12, 0, 0, 9],
                           [8, 0, 0, 5],
                           [13, 3, 2, 16]]), "3rd example"
