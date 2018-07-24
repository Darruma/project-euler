#euler2

fib = 0
a = 1
b = 1
sum = 0

while(fib < 4000000):
    if fib % 2 == 0:
        sum = fib + sum

    fib = a + b
    b = a
    a = fib

print(sum)
