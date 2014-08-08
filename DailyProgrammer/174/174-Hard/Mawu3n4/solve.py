
nb_points = int(raw_input())
points = []

for i in range(nb_points):
    u_input = raw_input().split(',')
    points.append((int(u_input[0].strip()), int(u_input[1].strip()), chr(i+65)))


points = sorted(set(points))

upper = []
lower = []

def ccw_check(p1, p2, p3):
    return (False
            if (p2[0] - p1[0])*(p3[1] - p1[1]) -
            (p2[1] - p1[1])*(p3[0] - p1[0]) > 0
            else True)

for p in points:
    while len(lower) >= 2 and ccw_check(lower[-2], lower[-1], p):
        lower.pop()
    lower.append(p)

for p in points[::-1]:
    while len(upper) >= 2 and ccw_check(upper[-2], upper[-1], p):
        upper.pop()
    upper.append(p)

upper.pop()
lower.pop()

res = "".join([x[-1] for x in upper]) + "".join([x[-1] for x in lower])
start = res.find('A')
print res[start:] + res[:start]

