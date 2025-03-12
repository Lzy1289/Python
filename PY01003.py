def lamtron(n):
    if n <= 10:
        return n
    fact = 10
    while n > fact:
        n = (n + fact // 2) // fact * fact
        fact *= 10
    return n

test = int(input())
for i in range(0, test, 1):
    n = int(input())
    print(lamtron(n))
