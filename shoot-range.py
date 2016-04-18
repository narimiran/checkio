from math import sqrt


def shot(wall1, wall2, shot_point, later_point):
    if wall2[0]-wall1[0] == 0:
        if later_point[0]-shot_point[0] == 0:  # both are vertical
            return -1
        else:  # wall is vertical
            shot_k = (later_point[1]-shot_point[1])/(later_point[0]-shot_point[0])
            impact_x = wall2[0]
            impact_y = shot_k * (impact_x - shot_point[0]) + shot_point[1]

    elif later_point[0]-shot_point[0] == 0:  # shooting vertically
        wall_k = (wall2[1]-wall1[1])/(wall2[0]-wall1[0])
        impact_x = shot_point[0]
        impact_y = wall_k * (impact_x - wall1[0]) + wall1[1]

    else:
        wall_k = (wall2[1]-wall1[1])/(wall2[0]-wall1[0])
        shot_k = (later_point[1]-shot_point[1])/(later_point[0]-shot_point[0])
        impact_x = (shot_point[1] - wall1[1] - (shot_k*shot_point[0] - wall_k*wall1[0])) / (wall_k - shot_k)
        impact_y = wall_k * (impact_x - wall1[0]) + wall1[1]

    wall_center = ((wall1[0]+wall2[0])/2, (wall1[1]+wall2[1])/2)
    wall_distance = sqrt((wall2[1]-wall_center[1])**2 + (wall2[0]-wall_center[0])**2)
    impact_distance = sqrt((impact_y-wall_center[1])**2 + (impact_x-wall_center[0])**2)

    score = 100 - (impact_distance/wall_distance) * 100

    shot_point_distance = sqrt((shot_point[1]-wall_center[1])**2 + (shot_point[0]-wall_center[0])**2)
    later_point_distance = sqrt((later_point[1]-wall_center[1])**2 + (later_point[0]-wall_center[0])**2)

    if score < 0 or shot_point_distance < later_point_distance:
        return -1  # missed or shooting in wrong direction
    else:
        return round(score, 0)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
