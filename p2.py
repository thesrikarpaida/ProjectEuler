def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter an upper limit for the Fibonacci terms:"))
s = 0
i = 1
x = fib(i)
while x <= n:
    if x%2 == 0:
        s = s + x
    i = i + 1
    x = fib(i)
print("Sum of Even Fibonacci terms upto ",n," is ",s)
