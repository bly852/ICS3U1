def persistence(n):
    #Calculations the persistence of a given whole number
    n = int(n)
    steps = 0
    
    #Runs multiplication while number is not a single digit
    while len(str(n)) != 1:
        newN = 1
        for x in str(n):
            newN*= int(x)
        n = newN
        
        #Records the number of steps it has taken
        steps +=1
    return steps
print(persistence(389))