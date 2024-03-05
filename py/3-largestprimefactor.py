#This solution is not mine, I skipped this one myself and someone I was helping decided to not skip it. Only changes ive made is the print statement and starting and incrementing the factors to only be odd

number = 600851475143
factor = 3
factors = []

while factor ** 2 <= number:
    if number % factor == 0:
        second_factor = 3
        is_prime = True
        while second_factor ** 2 <= factor:
            if factor % second_factor == 0:
                is_prime = False
            second_factor += 2
        if is_prime:
            factors.append(factor)
    factor += 2

print(max(factors))
