def checkio(matrix):
    seen = set()
    all_groups = []
    height, width = len(matrix), len(matrix[0])

    for row in range(height):
        for col in range(width):
            if (row, col) not in seen:
                stack = [(row, col)]
                group = {(row, col)}
                group_value = matrix[row][col]
                while stack:
                    y, x = stack.pop()
                    seen.add((y, x))
                    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nx, ny = (x + dx, y + dy)
                        if (0 <= nx < width and 0 <= ny < height
                            and (ny, nx) not in seen
                            and matrix[ny][nx] == group_value):
                            group |= {(ny, nx)}
                            stack.append((ny, nx))
                all_groups.append(group)
    largest_group = max(all_groups, key=len)
    row, col = next(iter(largest_group))
    return [len(largest_group), matrix[row][col]]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
