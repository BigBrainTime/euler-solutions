#In Progress
import primes
value = 600851475143
it = 2
while True:
    if value%it==0 and primes.is_prime(it):
        break

print(it)