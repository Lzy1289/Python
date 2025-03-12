import math

def isprime(x):
    if x==2: return True
    if x<2: return False
    if x%2==0: return False
    for i in range(3,int(sqrt(x))+1,2):
        if x%i==0: return False
    return True

t = int(input())
for i in range(0,t,1):
    n = int(input())
    result = math.gcd(n, )
    if result == 1:
        print("YES")
    else:
        print("NO")


