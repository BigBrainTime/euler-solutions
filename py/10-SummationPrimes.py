value = 2000000
primes = []
n = 2

while n < value:
    boolcheck = []

    if len(primes) <= 10:
        for i in range(2,n//2):
            if n % i == 0:
                #divideable
                boolcheck.append(False)
                break

            else:
                boolcheck.append(True)

    else:
        for i in primes:
            if n % i == 0:
                #divideable
                boolcheck.append(False)
                break

            else:
                boolcheck.append(True)

    if False not in boolcheck and n != 4:
        primes.append(n)

    n+=1

print(sum(primes))