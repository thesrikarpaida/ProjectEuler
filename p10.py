n = int(input())
s = 2
for i in range(3,n):
    c = 0
    for j in range(2,i):
        if i%j == 0:
            c = 1
            break
    if c == 0:
        s+=i
print(s)
