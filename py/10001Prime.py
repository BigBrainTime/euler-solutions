prime = 0
n = 2
boolcheck = []

while prime < 10001:
    boolcheck = []

    for i in range(2,n//2):
        if n % i == 0 or n == 4:
            #divideable
            boolcheck.append('False')
            break

        elif n != 4:
            #potentially dividable
            boolcheck.append('True')

    if 'False' not in boolcheck and n != 4:
        prime += 1
        print(n,'is the',prime,'prime')

    n += 1

print(n-1)