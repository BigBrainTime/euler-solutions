import threading
value = 2000000
threads = 10
sums = [2]
n = 3

def isprime(start, end):
    lsum = 0
    for k in range(start, end, 2):
        boolcheck = []

        for i in range(2,k//2):
            if k % i == 0:
                boolcheck.append(False)
                break

            else:
                boolcheck.append(True)

        if False not in boolcheck:
            lsum += k
    sums.append(lsum)
    

ends = []
starts = []
for x in range(threads):
    ends.append((value//threads)*(x+1))
    starts.append(((value//threads)*x)+1)
starts[0] = n

for t in range(threads):
    globals()[f"thread_{t}"] = threading.Thread(target=(isprime), args=(starts[t], ends[t]))
    globals()[f"thread_{t}"].start()

for t in range(threads):
    globals()[f"thread_{t}"].join()

print(sum(sums))