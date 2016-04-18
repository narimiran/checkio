def find_word(message):
    results = {}
    words = ''.join(ch for ch in message.lower() if ch not in '.,?!').split()
    for i, word_1 in enumerate(words):
        score = 0
        other_words = words[:i] + words[i+1:]
        for word_2 in other_words:
            score += 10 * (word_1[0] == word_2[0])
            score += 10 * (word_1[-1] == word_2[-1])
            score += 30 * min(len(word_1)/len(word_2), len(word_2)/len(word_1))
            unique = len(set(word_1) | set(word_2))
            common = len(set(word_1) & set(word_2))
            score += 50 * common / unique
        results[word_1] = round(score / (len(other_words)), 3)

    for word in words[::-1]:
        if results[word] == max(results.values()):
            return word


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
