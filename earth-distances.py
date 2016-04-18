from math import pi, acos, sin, cos

def get_radians(coord):
    for s in u"°′″":
        coord = coord.replace(s, ' ')
    coord = coord.split()
    degs = int(coord[0]) + int(coord[1])/60 + int(coord[2])/3600
    rads = degs * pi / 180
    direction = coord[3][0]
    if direction == 'W' or direction == 'S':
        return -rads
    return rads


def distance(first, second):
    R = 6371
    if len(first.split()) == 2:
        f_lat, f_long = first.split()
    else:
        f_lat, f_long = first.split(',')
    if len(second.split()) == 2:
        s_lat, s_long = second.split()
    else:
        s_lat, s_long = second.split(',')

    f1 = get_radians(f_lat)
    l1 = get_radians(f_long)
    f2 = get_radians(s_lat)
    l2 = get_radians(s_long)

    delta_sigma = acos(sin(f1)*sin(f2) + cos(f1)*cos(f2)*cos((l2 - l1)))
    if delta_sigma == 0:
        return R * pi
    return R * delta_sigma


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
