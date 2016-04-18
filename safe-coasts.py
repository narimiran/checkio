def finish_map(regional_map):
    sea_map = [[char for char in row] for row in regional_map]

    # mark all coastal tiles
    for i, row in enumerate(sea_map):
        for j, tile in enumerate(row):
            if tile == 'X':
                left = max(0, j-1)
                right = min(len(sea_map[0]), j+2)
                top = max(0, i-1)
                bottom = min(len(sea_map), i+2)

                for r in range(top, bottom):
                    for c in range(left, right):
                        if sea_map[r][c] == '.':
                            sea_map[r][c] = 'S'

    # sail to all reachable uncharted tiles
    finished = False
    while not finished:
        finished = True
        for i, row in enumerate(sea_map):
            for j, tile in enumerate(row):
                if tile == '.':
                    left = max(0, j-1)
                    right = min(len(sea_map[0])-1, j+1)
                    top = max(0, i-1)
                    bottom = min(len(sea_map)-1, i+1)

                    if ('D' in sea_map[top][j] or
                        'D' in sea_map[bottom][j] or
                        'D' in sea_map[i][left] or
                        'D' in sea_map[i][right]):
                        sea_map[i][j] = 'D'
                        finished = False

    # mark unreachable tiles as safe
    return [''.join(row).replace('.', 'S') for row in sea_map]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"
