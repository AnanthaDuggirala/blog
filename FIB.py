i = 0
num = int(input("Enter a number and check the fibonanci series until that: "))
fib = []
for n in range(num):
    if(n == 0):
        fib.append(0)
    elif (n == 1):
        fib.append(1)
    else:
        fib.append(fib[n-1] + fib[n-2])

print(fib)
