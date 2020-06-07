import sys

n = int(input())
i = 0
j = 2
m = 0
while j > 0:
    c = 0
    for k in range(2,j):
        if j%k == 0:
            c = 1
            break
    if c == 0:
        i = i + 1
    if i == n:
        print(j)
        sys.exit(0)
    j = j + 1

