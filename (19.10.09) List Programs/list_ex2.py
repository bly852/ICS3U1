n = [1, 7, 4, 8, 3, 6, 2, 0]

print("List multiplied by two:", end=" ")
for x in range(len(n)):
    print(n[x]*2, end= " ")

nSum = str(sum(n)/len(n))
print("\nMedian of the list: " + nSum)

nSum2 = str(sum(n)*2/len(n))
print("Median of the list multiplied by two: " + nSum2)