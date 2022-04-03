sqr = 0
sumsqr = []

for i in range(101):
    sqr += i**2
    sumsqr.append(i)

print(sum(sumsqr)**2 - sqr)