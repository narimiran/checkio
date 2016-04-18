def checkio(number):
    triangles = [n*(n+1)//2 for n in range(1, 32)]
                 # 31st+32nd triangular > max number
    for a in range(32):
        for b in reversed(range(32)):
            if sum(triangles[a:b]) == number:
                return triangles[a:b]
    return []


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
