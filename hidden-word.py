from itertools import zip_longest


def checkio(text, word):
    horizontal = text.lower().replace(' ', '').splitlines()
    for i, row in enumerate(horizontal, 1):
        index = row.find(word)
        if index >= 0:
            return [i, index+1, i, index+len(word)]

    vertical = [''.join(line) for line in zip_longest(*horizontal, fillvalue='-')]
    for i, col in enumerate(vertical, 1):
        index = col.find(word)
        if index >= 0:
            return [index+1, i, index+len(word), i]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]