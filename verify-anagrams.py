def verify_anagrams(first_word, second_word):
    a = sorted([letter for letter in first_word.lower() if letter.isalpha()])
    b = sorted([letter for letter in second_word.lower() if letter.isalpha()])
    return a == b


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
