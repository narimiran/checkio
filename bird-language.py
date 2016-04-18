VOWELS = "aeiouy"

def translate(phrase):
    human_phrase = []
    i = 0

    while i < len(phrase):
        human_phrase.append(phrase[i])
        if phrase[i] in VOWELS:
            i += 3
        elif phrase[i] == ' ':
            i += 1
        else:
            i += 2
    return ''.join(human_phrase)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
