chain = 0
num = 0

def next(n):
    if n%2 == 0:
        n /= 2
    else:
        n = ((3*n) + 1)
    return int(n)

for i in range(1, 1000000):
    n = i
    k = 0

    while True:
        if next(n) == 1:
            break
        else:
            n = next(n)
            k += 1

    if k > chain:
        chain = k
        num = i

print(num, chain)