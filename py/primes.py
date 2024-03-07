import os
from math import sqrt

def get_primes():
    with open(os.path.join(os.getcwd(), 'py', 'primes.txt'), 'r') as file:
        return list(map(int,file.read().split('\n')[:-1]))

def next_prime():
    primes = get_primes()
    prime = int(primes[-1])
    l = len(primes)
    while l == len(primes):
        boolcheck = True
        prime += 2
        for i in primes:
            boolcheck = bool(prime % i)
            if not boolcheck or i >= sqrt(prime):
                break

        if boolcheck:
            primes.append(prime)
    with open(os.path.join(os.getcwd(), 'py', 'primes.txt'), 'a') as file:
        file.write(f'{prime}\n')
    return primes

def get_prime(nth):
    primes = get_primes()
    while len(primes) < nth+1:
        primes = next_prime()
    return primes[nth-1]

def get_n_primes(start,end):
    get_prime(end)
    return get_primes()[start-1:end]

def is_prime(value):
    primes = get_primes()
    try:
        primes.index(value)
        return True
    except ValueError:
        pass
    while primes[-1] < sqrt(value):
        primes=next_prime()

    boolcheck = True

    for i in primes:
        boolcheck=(bool(value % i))
        if not boolcheck or i >= sqrt(value):
            break

    if boolcheck:
        return True
    return False

def find_nth_value(value, direction='<'):
    if value%2 ==0:
        if direction == '<':
            value -= 1
        elif direction == '>':
            value += 1
        else:
            raise AttributeError('Invalid Direction, < and > only')

    while not is_prime(value):
        if direction == '<':
            value -= 2
        elif direction == '>':
            value += 2

    primes = get_primes()

    try:
        return primes.index(value)+1#+1 bc primes.txt counts from 1
    except ValueError:
        pass

    while value not in primes:
        primes=next_prime()

    return primes.index(value)+1