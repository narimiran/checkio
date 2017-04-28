def subnetworks(net, crushes):
    crushes = set(crushes)
    cities = 0
    visited = set()
    alive = {node for connection in net for node in connection
             if node not in crushes}

    for start in alive:
        if start not in visited:
            stack = {start}
            while stack:
                current = stack.pop()
                visited |= {current}
                for left, right in net:
                    if right == current:
                        left, right = right, left
                    if left == current and right not in visited | crushes:
                        stack |= {right}
            cities += 1
    return cities


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
