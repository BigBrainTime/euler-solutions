it = 1000
div = 500
primes=[2,3,5,7,9,11,13,17,19]

def generate(n):
    return sum(range(n+1))


def next_prime():
    calculate = True
    p=primes[-1]+2
    while calculate:
        boolcheck=[]
        for i in primes:
            boolcheck.append(bool(p % i))
            if not boolcheck[-1]:
                break

        if False not in boolcheck:
            primes.append(p)
            calculate=False
            break
        p+=2

def divisors(n):
    divisors = 1
    original = n
    while True:
        for prime in primes:
            while True:
                if n % prime != 0:
                    break
                divisors += int(not bool(n % prime))
                n = n/((prime*int(not bool(n % prime)))+int(bool(n % prime)))
        
        if n < primes[-1]:
            break
        next_prime()

    print(divisors,len(primes))
    return divisors


while (divisors(generate(it)) < div):
    it += 1

print(generate(it))
