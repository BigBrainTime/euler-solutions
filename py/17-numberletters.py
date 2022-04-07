ones = ["one","two","three","four","five","six","seven","eight","nine"]
tens = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
specials = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
string = ""

for i in range(1,1001):
    num = list(map(int, str(i)))
    if len(num) == 3:
        if num[1] != 0 and num[2] != 0 and num[1] != 1:
            string += ones[num[0]-1] + "hundredand"
            string += tens[num[1]-1]
            string += ones[num[2]-1]
        elif num[1] != 0 and num[2] == 0:
            string += ones[num[0]-1] + "hundredand"
            string += tens[num[1]-1]
        elif num[1] == 1:
            string += ones[num[0]-1] + "hundredand"
            string += specials[num[2]-1]
        elif num[1] == 0 and num[2] != 0:
            string += ones[num[0]-1] + "hundredand"
            string += ones[num[2]-1]
        elif num[1] == 0 and num[2] == 0:
            string += ones[num[0]-1] + "hundred"

    elif len(num) == 2 and num[0] != 1:
        string += tens[num[0]-1]
        if num[1] != 0:
            string += ones[num[1]-1]

    elif len(num) == 2 and num[0] == 1:
        if num[1] != 0:
            string += specials[num[1]-1]
        else:
            string += tens[0]

    elif len(num) == 1:
        string += ones[num[0]-1]

    else:
        string += "onethousand"
print(len(string))