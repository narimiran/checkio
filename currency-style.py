def checkio(text):
    words = text.split(' ')
    result = []
    for word in words:
        if word.startswith('$'):
            if word.endswith(',') or word.endswith('.'):
                front = word[:-4].replace('.', ',')
                back = word[-4:-1].replace(',', '.', 1)
                rest = word[-1]
                new_word = front + back + rest
            else:
                front = word[:-3].replace('.', ',')
                back = word[-3:].replace(',', '.', 1)
                new_word = front + back
            result.append(new_word)
        else:
            result.append(word)
    return ' '.join(result)


if __name__ == '__main__':    

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    assert checkio("$0,89") == "$0.89" , "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"
