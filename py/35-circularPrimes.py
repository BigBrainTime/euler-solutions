#In Progress - Works for < 1000
import primes

currentprime = 1

found = []

prime = primes.get_prime(currentprime)
while prime < 1000:
    if len(set(str(prime))) == 1: #all numbers where all digits are the same(includes single digits)
        variations = [prime]
    elif len(str(prime)) == 2:
        variations = (int(f'{str(prime)[0]}{str(prime)[1]}'), int(f'{str(prime)[1]}{str(prime)[0]}'))
    elif len(str(prime)) == 3:
        variations = (int(f'{str(prime)[0]}{str(prime)[1]}{str(prime)[2]}'), int(
            f'{str(prime)[0]}{str(prime)[2]}{str(prime)[1]}'), int(f'{str(prime)[1]}{str(prime)[0]}{str(prime)[2]}'), int(
            f'{str(prime)[1]}{str(prime)[2]}{str(prime)[0]}'), int(f'{str(prime)[2]}{str(prime)[0]}{str(prime)[1]}'), int(
            f'{str(prime)[2]}{str(prime)[1]}{str(prime)[0]}'))
    
    boolcheck = True
    for variation in variations:
        boolcheck=(primes.is_prime(variation))
        if not boolcheck:
            break
    if boolcheck:
        found += variations

    currentprime += 1
    prime = primes.get_prime(currentprime)
    while prime in found:
        currentprime += 1
        prime = primes.get_prime(currentprime)

print(found)