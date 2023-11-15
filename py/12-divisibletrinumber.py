# Takes way too long but works
it = 2
div = 200


def generate(n):
    return sum(range(n+1))


def divisors(n):
    divisors = 2
    for i in range(2, (n//2)+1):
        divisors += int(not bool(n % i))
    return divisors


while divisors(generate(it)) < div:
    it += 1

print(generate(it-1))
