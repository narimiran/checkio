def checkio(game_result):
    sample = ''.join(game_result)
    all_possibilities = (game_result +
                         [sample[i::3] for i in range(3)] +
                         [sample[0::4]] +
                         [sample[2:7:2]])
    if 'XXX' in all_possibilities:
        return 'X'
    elif 'OOO' in all_possibilities:
        return 'O'
    else:
        return 'D'
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

