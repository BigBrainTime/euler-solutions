#Takes way too long but works
check = True
it = 2
div = 500

def generate(n):
    return sum(range(n+1))

def divisors(n):
    divisors = 2
    for i in range(2,(n//2)+1):
        if n % i == 0:
            divisors += 1
    return divisors

while check:
    if divisors(generate(it)) > div:
        check = False
    it += 1

print(generate(it-1))