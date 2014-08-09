
nb_points = int(raw_input())
points = []

for i in range(nb_points):
    u_input = raw_input().split(',')
    points.append((int(u_input[0].strip()), int(u_input[1].strip()), chr(i+65)))

points = sorted(set(points))

upper = []
lower = []

# Return True if p1, p2, and p3 make a counter clockwise turn
# False otherwise
def ccw_check(p1, p2, p3):
    return (False
            if (p2[0] - p1[0])*(p3[1] - p1[1]) -
            (p2[1] - p1[1])*(p3[0] - p1[0]) > 0
            else True)

# Computer the points of the lower part of the convex hull
for p in points:
    # If 3 successive points make a counter clockwise turn, then one of them
    # should not be part of the perimeter
    while len(lower) >= 2 and ccw_check(lower[-2], lower[-1], p):
        lower.pop()
    lower.append(p)

# Computer the upper part
for p in points[::-1]:
    while len(upper) >= 2 and ccw_check(upper[-2], upper[-1], p):
        upper.pop()
    upper.append(p)

# The last point is the same as the first one of the other part
upper.pop()
lower.pop()

res = "".join([x[-1] for x in upper]) + "".join([x[-1] for x in lower])
start = res.find('A')
print res[start:] + res[:start]

