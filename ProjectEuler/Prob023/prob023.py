import math

def is_abundant(n):
    res = 1
    n_sqrt = int(math.sqrt(n))
    if n_sqrt * n_sqrt == n:
        res += n_sqrt
    else:
        n_sqrt += 1
    res += sum(i + n/i for i in range(2, n_sqrt) if not n % i)
    return res > n

def is_sum(n, l):
    for i in reversed(range(1, len(l))):
        if (n - l[i]) in l[:i]:
            return True
    return False

ab_num = [n for n in range(12, 28124) if is_abundant(n)]

abundant_sums = [0] * 28124

for i in range(len(ab_num)):
    for j in range(len(ab_num)):
        if ab_num[i] + ab_num[j] <= 28123:
            abundant_sums[ab_num[i] + ab_num[j]] = 1
        else:
            break

res = sum(n for n in range(1, 28124) if not abundant_sums[n])

print res
