n = int(input("Enter a number: "))
fib1 = 0
fib2 = 1
print("\nYour Fibonacci numbers are: ")
for x in range (1, n+1):
    print (fib1, end=" ")
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib