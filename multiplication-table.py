def checkio(first, second):
    total = 0
    for operator in ('&', '|', '^'):
        tot_row = 0
        for i in bin(first)[2:]:
            row = ''
            for j in bin(second)[2:]:
                row += eval('str(int(i) {} int(j))'.format(operator))
            tot_row += int(row, 2)
        total += tot_row
    return total


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18