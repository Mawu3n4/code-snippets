
def looknsay(seed):
    numbers = seed
    while True:
        yield numbers
        count = 0
        res = ''
        for i, n in enumerate(numbers[1:]):
            if n == numbers[i]:
                count += 1
            else:
                res += str(count+1)+numbers[i]
                count = 0

        numbers = res+str(count+1)+numbers[-1]


gen = looknsay(str(input("Seed ?: ")))

for i in range(input("Nth ?: ") - 1):
    gen.next()

print gen.next()
