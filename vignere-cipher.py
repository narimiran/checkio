from itertools import cycle
from string import ascii_uppercase as alphabet


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    key = [(ord(e)-ord(d)) % 26 for d, e in zip(old_decrypted, old_encrypted)]

    for key_length in range(2, len(key)):
        if all(len(set(key[j::key_length])) == 1 for j in range(key_length)):
            key = key[:key_length]
            break

    return ''.join(alphabet[(ord(e) - ord('A') - k) % 26]
                   for k, e in zip(cycle(key), new_encrypted))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
