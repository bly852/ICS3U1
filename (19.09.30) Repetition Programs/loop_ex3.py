n = int(input("Enter a number: "))
divisor = n
print("\nExact Divisors:", end=" ")
for x in range (1, n+1):
    remain = n%divisor
    if remain == 0:
        print (int(n/divisor), end=", ")
    divisor = divisor-1