def longest_palindromic(text):
    for size in reversed(range(len(text))):
        for start in range(len(text) - size):
            sample = text[start:][:size+1]
            if sample == sample[::-1]:
                return sample


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
