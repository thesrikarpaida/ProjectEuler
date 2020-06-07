n = int(input())
c = 0
for i in range(0,n):
    ch = 1
    while i != 1:
        if i%2 == 0:
            i = i/2
            ch+=1 
        else:
            i = 3*i + 1
            ch+=1
    c = max(c,ch)
print(c)
