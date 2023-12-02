it = 20
divcheck = [11,12,13,14,15,16,17,18,19]

while True:
    boolcheck = []

    for div in divcheck:
        boolcheck.append(not bool(it % div))
        if not boolcheck[-1]:
            break

    if boolcheck[-1]:
        print(it)
        quit()

    it += 20