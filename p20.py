import math

n = int(input())
s = 0
for i in str(math.factorial(n)):
    s+=int(i)
print(s)
