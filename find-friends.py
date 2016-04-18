def check_connection(network, first, second):
    visited = set()
    stack = {first}
    while stack:
        current = stack.pop()
        visited |= {current}
        for connection in network:
            left, right = connection.split('-')
            if right == current:
                left, right = right, left
            if left == current and right not in visited:
                if right == second:
                    return True
                stack |= {right}
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
