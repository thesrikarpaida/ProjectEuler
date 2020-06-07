n = int(input())
i = 2
c = 0
while c < n:
    s = int(i*(i+1)/2)
    c = 0
    for j in range(1,s):
        if s%j == 0:
            c = c + 1
    i = i + 1
print(s)
