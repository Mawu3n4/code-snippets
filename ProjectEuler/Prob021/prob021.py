import sys

if len(sys.argv) != 2:
    print "Usage: solve.py [TRIANGLE FILE]"
    sys.exit(1)

with open(sys.argv[1]) as f:
    triangle = [ [int(n) for n in line.strip().split(' ')]
                 for line in f ]

for i in reversed(range(0, len(triangle) - 1)):
    for j, n in enumerate(triangle[i]):
        triangle[i][j] = max(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]

print triangle[0][0]
