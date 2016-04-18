def checkio(teleports_string):
    available_edges = set(teleports_string.split(','))
    stack = [('1', available_edges)]

    while stack:
        my_route, available_edges = stack.pop()

        if len(set(my_route)) == 8 and my_route.endswith('1'):
            return my_route

        next_stops = (c for c in available_edges if my_route[-1] in c)
        for stop in next_stops:
            stack.append((my_route + stop.strip(my_route[-1]),
                          available_edges-{stop}))


# This part is using only for self-testing

if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for  x, y in
                         teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if teleport not in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"),  \
        "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,"
                                   "56"),  "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"),  \
        "Fourth"