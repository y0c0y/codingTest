n1 = int(input())
n2 = int(input())

third = (n2 % 10) * n1
print(third)

second = ((n2 // 10) % 10) * n1
print(second)
    
second = second * 10

first = (n2 // 100) * n1
print(first)
    
first = first * 100

result = first + second + third
print(result)