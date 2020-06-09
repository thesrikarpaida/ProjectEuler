import math

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter the number of digits:"))
ans = 0
i = 1
while i > 0:
    d = int(math.log10(fib(i))) + 1
    if d == n:
        ans = i
        break
    else:
        i = i + 1

print(ans)
