def cut_sentence(line, length):
    if len(line) <= length:
        return line

    while len(line) > length:
        line = ' '.join(line.split()[:-1])
    return line + '...'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "First"
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Third"
    print('Done')
