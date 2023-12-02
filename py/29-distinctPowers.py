lst=[]
intrange=range(2,101)
exprange=range(2,101)

for exp in exprange:
    for integer in intrange:
        num = integer**exp
        if num not in lst:
            lst.append(num)

print(len(lst))