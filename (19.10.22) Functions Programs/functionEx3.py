def persistence(n):
    """persistence (n) - returns the persistence of the parameter n"""
    n = int(n)
    steps = 0
    
    # Runs multiplication while number is not a single digit
    while len(str(n)) != 1:
        new_n = 1
        for x in str(n):
            new_n *= int(x)
        n = new_n
        
        # Records the number of steps it has taken
        steps += 1
    return steps


print(persistence(389))
