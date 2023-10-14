def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())
numberList = list(map(int, input().split()))
cntOfPrime = 0

for n in numberList:
    if n == 1 :
        continue
    if isPrime(n):
        cntOfPrime += 1
print(cntOfPrime)
