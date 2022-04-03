check = 1
it = 0
boolcheck = []
divcheck = [11,12,13,14,15,16,17,18,19,20]

while check == 1:
    boolcheck = []

    for i in range(len(divcheck)):
        remainder = it%(divcheck[i])

        if remainder == 0:
            boolcheck.append('True')
        else:
            boolcheck.append('False')
            break

    if 'False' not in boolcheck and it != 0:
        check = 0

        print(it,' has passed')

    it += 20