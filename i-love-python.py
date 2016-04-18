def i_love_python():
    sentence = "I realy do love coding in Python!".split()
    return ' '.join(sentence[::3])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
