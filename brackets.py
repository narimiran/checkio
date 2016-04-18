def checkio(expression):
    a = [e for e in expression if e in '{[()]}']
    print(a)
    brackets = {'{': '}',
                '[': ']',
                '(': ')'}
    stack = []
    for char in a:
        if char in brackets.keys():
            stack.append(char)
        elif not stack or brackets[stack.pop()] != char:
                return False
    return not stack


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
