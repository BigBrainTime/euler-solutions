chain = 0

for i in range(1, 1000000):
    n = i
    k = 0

    while n != 1:
        n = ((n/2)*int(bool(n % 2 == 0)))+(((3*n) + 1)*int(bool(n % 2 != 0)))
        k += 1

    if k > chain:
        chain = k
        num = i

print(num, chain)