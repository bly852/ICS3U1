def occ(s1,s2):
    #finds the number of times s2 occurs in s1
    count = 0
    start = 0
    while True:
        search = s1.find(s2,start)
        
        if search == -1:
            break
        else:
            count +=1
            start = search+1
    return count