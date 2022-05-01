prime = 0
primes = []
n = 2

while prime < 10001:
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
        prime += 1

    n += 1

print(n-1)