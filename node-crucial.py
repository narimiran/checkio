from collections import defaultdict

def most_crucial(net, users):
    def subnetworks(crush):
        score = users[crush]
        total_visited = set()
        alive = {node for connection in net for node in connection
                 if node != crush}

        for start in alive:
            if start not in total_visited:
                visited = set()
                stack = {start}
                while stack:
                    current = stack.pop()
                    visited |= {current}
                    for left, right in net:
                        if right == current:
                            left, right = right, left
                        if left == current and right not in visited | {crush}:
                            stack |= {right}
                total_visited |= visited
                score += sum(v for k, v in users.items() if k in visited) ** 2
        return score

    results = defaultdict(list)
    for k in users.keys():
        results[subnetworks(k)].append(k)
    return results[min(results)]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')
