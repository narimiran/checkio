def digit_stack(commands):
    total = 0
    stack = []

    for command in commands:
        if command[:2] == "PU":
            stack.append(command[-1])
        elif stack:
            total += int(stack[-1])
            if command[:2] == "PO":
                stack.pop()
    return total

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
