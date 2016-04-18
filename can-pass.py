def can_pass(matrix, first, second):
    visited = set()
    stack = {first}
    path = matrix[first[0]][first[1]]
    height, width = len(matrix), len(matrix[0])

    while stack:
        neighbours = set()
        for cy, cx in stack:
            visited.add((cy, cx))
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = (cx + dx, cy + dy)

                if (0 <= nx < width and 0 <= ny < height
                    and (ny, nx) not in visited
                    and matrix[ny][nx] == path
                    ):
                    neighbours |= {(ny, nx)}
        stack = neighbours

    return second in visited


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
