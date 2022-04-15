import os, string

path = f"{os.getcwd()}/22-names/p022_names.txt"  #if running this yourself your working directory may be different meaning this line may not work
alph = list(string.ascii_uppercase)
score = 0

with open(path,'r') as names:
    namelist = sorted(names.read().replace('"', '').split(","))

for name in namelist:
    temp = 0
    for letter in name:
        temp += alph.index(letter)+1

    score += temp*(namelist.index(name)+1)

print(score)