#In progress

import primes

found = []
nthprime = 5    #Number 11

while len(found) < 11:
    masterprime = primes.get_prime(nthprime)
    currentprime = str(masterprime)
    if len(currentprime) >= 3:
        all_primes = True
        while len(currentprime) > 1:
            currentprime = currentprime[1:]
            is_prime = primes.is_prime(int(currentprime))
            all_primes = is_prime if all_primes and is_prime else False
            if not all_primes:
                break

        if all_primes:
            currentprime = str(masterprime)
            while len(currentprime) > 1:
                print(currentprime, currentprime[:-1])
                currentprime = currentprime[:-1]
                is_prime = primes.is_prime(int(currentprime))
                all_primes = is_prime if all_primes and is_prime else False
                if not all_primes:
                    break

        if all_primes:
            found.append(masterprime)
    nthprime += 1

print(found)
print(sum(found))