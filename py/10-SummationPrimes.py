value = 2000000
primes = []
n = 2

while n < value:
    boolcheck = []

    for i in primes:
        boolcheck.append(bool(n % i))
        if not boolcheck[-1]:
            break

    if False not in boolcheck:
        primes.append(n)

    n+=1

print(sum(primes))