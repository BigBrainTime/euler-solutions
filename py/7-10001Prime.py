prime = 0
n = 2

while prime < 10002: #one extra bc for some reason 4 is counted as a prime
    boolcheck = []

    for i in range(2,n//2):
        if n % i == 0:
            #divideable
            boolcheck.append(False)
            break

        else:
            boolcheck.append(True)

    if False not in boolcheck:
        prime += 1

    n += 1

print(n-1)