sqr = 0
sumsqr = []
sumsqr2 = 0

for i in range(101):
    sqr += i**2
    sumsqr.append(i)

sumsqr2 = sum(sumsqr)**2

print(sumsqr2 - sqr)