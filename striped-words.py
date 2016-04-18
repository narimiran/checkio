VOWELS = set("AEIOUY")
CONSONANTS = set("BCDFGHJKLMNPQRSTVWXZ")

def checkio(text):
    txt = ''.join(c.upper() if c.isalnum() else ' ' for c in text).split()
    total = 0
    for word in txt:
        if len(word) < 2:
            continue
        odd = set(word[1::2])
        even = set(word[::2])
        total += ((odd <= VOWELS and even <= CONSONANTS) or
                  (odd <= CONSONANTS and even <= VOWELS))
    return total


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
