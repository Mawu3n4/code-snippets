
# n = order in the diagonal
# Center to Upper-right = 4n^2 - 4n + 1
# Center to Lower-right = 4n^2 - 4n + 1 + 2n
# Center to Lower-left = 4n^2 - 4n + 1 + 4n
# Center to Upper-left = 4n^2 - 4n + 1 + 6n
# or
# 4n^2 + 1 + (2m - 4)n with m = 0 to number of diagonals and n = order from 1 to size/2+1

size = 1001

def spiral(n, m):
    return 4 * n * n + (2 * m - 4) * n + 1

print sum(set(spiral(n, m)
          for m in range(0, 4)
          for n in range(size/2+1))) + spiral(size/2+1, 0)

