prime = 2
primes = [2, 3]
n = 3
boolcheck = []

while prime < 10001:
    boolcheck = []

    for i in primes:
        boolcheck.append(bool(n % i))
        if not boolcheck[-1]:
            break

    if False not in boolcheck:
        prime += 1
        primes.append(n)

    n += 2

print(n-2)