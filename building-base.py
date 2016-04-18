from itertools import product

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.north = south + width_NS
        self.east = west + width_WE
        self.width_x = width_WE
        self.width_y = width_NS
        self.height = height

    def corners(self):
        corners_ = product({'south', 'north'}, {'west', 'east'})
        return {'-'.join(c): [getattr(self, v) for v in c] for c in corners_}

    def area(self):
        return self.width_x * self.width_y

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return ('Building({0.south}, {0.west}, {0.width_x}, '
                         '{0.width_y}, {0.height})'.format(self))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
