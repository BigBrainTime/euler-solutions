chain = 0
num = 0

def next(n):
    #n = ((n/((int(not bool(n % 2))*2)+int(bool(n % 2))))*int(not bool(n % 2)))+(((3*n) + 1)*int(bool(n % 2)))
    if n%2 == 0:
        n /= 2
    else:
        n = ((3*n) + 1)
    return int(n)

for i in range(1, 1000000):
    n = i
    k = 0

    while next(n) != 1:
        n = next(n)
        k += 1

    if k > chain:
        chain = k
        num = i

print(num, chain)