
pth = []
prod = 1

def cbreak(a,b,c):
    global pth,prod

    if a**2 + b**2 == c**2 and a + b + c == 1000 and a > 0 and b > 0 and c > 0:

        if pth == []:
            pth = [a,b,c]
            
            for i in range(3):
                prod *= pth[i]

            print(prod)

for a in range(1000):
    for b in range(1000):
        cbreak(a,b,1000-(a+b))
        
        if prod != 1:
            break
    if prod != 1:
        break