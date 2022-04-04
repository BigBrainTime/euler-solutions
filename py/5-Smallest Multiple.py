check = True
it = 20
divcheck = [11,12,13,14,15,16,17,18,19]

while check:
    boolcheck = []

    for i in range(len(divcheck)):
        if it%(divcheck[i]) == 0:
            boolcheck.append(True)
        else:
            boolcheck.append(False)
            break

    if False not in boolcheck:
        check = False
        print(it,'has passed')

    it += 20