def recall_password(grille, pw):
    solution = []
    for _ in range(4):
        for rows in zip(grille, pw):
            for g, p in zip(*rows):
                if g == 'X':
                    solution.append(p)
        grille = list(zip(*grille[::-1]))
    return ''.join(solution)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
