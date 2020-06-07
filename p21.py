def sumOfDiv(n):
    s = 1
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            s+=i
            if i!=n/i:
                s+=x/i
    return int(s)

def isAmicable(a, b):

n = int(input())
