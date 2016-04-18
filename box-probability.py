def prob(white, black, step):
    white_prob = white / (white+black)
    black_prob = 1 - white_prob

    if step == 1:
        return white_prob

    else:
        pick_white = white_prob * prob(white-1, black+1, step-1)
        pick_black = black_prob * prob(white+1, black-1, step-1)
        return pick_white + pick_black


def checkio(marbles, step):
    return round(prob(marbles.count('w'), marbles.count('b'), step), 2)



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
