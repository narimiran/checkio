def checkio(stairs):
    if not stairs:
        return 0

    current_step, *remaining = stairs
    if not remaining:
        return max(current_step, 0)

    else:
        next_step, *next_remaining = remaining
        return max(current_step + checkio(remaining),
                   next_step + checkio(next_remaining))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, 'Second'
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, 'Third'
    print('All ok')