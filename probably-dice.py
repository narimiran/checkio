from math import factorial

def choose(a, b):
    if b == 0 or a == b:
        return 1
    else:
        numer = factorial(a)
        denom = factorial(b) * factorial(a-b)
        return numer//denom

def probability(n, s, p):
    k_max = (p-n)//s
    try:
        return 1/(s**n) * sum((-1)**k * choose(n, k) * choose(p-s*k-1, n-1) for k in range(0, k_max+1))
    except ValueError:
        return 0


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
