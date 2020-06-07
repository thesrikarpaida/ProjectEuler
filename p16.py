n,p = map(int,input().split())
s = 0
for i in str(n**p):
    s+= int(i)
print(s)
