def markAvgMean(marks):
    """
    markAvgMean (marks) - returns the average mean of the top 6 marks in the list of marks given
    """
    top6 = []
    for x in marks:
        if len(top6) >= 6:
            if x > min(top6):
                top6.pop(top6.index(min(top6)))
                top6.append(x)
        else:
            top6.append(x)
    return sum(top6)//6


def markAvgMedian(marks):
    """
    markAvgMedian (marks) - returns the average median of the top 6 marks in the list of marks given
    """
    top6 = []
    for x in marks:
        if len(top6) >= 6:
            if x > min(top6):
                top6.pop(top6.index(min(top6)))
                top6.append(x)
        else:
            top6.append(x)
    top6.sort()
    return top6[2]


# creates a list to store courses and their marks
marks = []

# infinite loop
while True:
    # asks user for course mark, ends loop when '-1 is entered
    mark = int(input('\nCourse Mark: '))
    if mark == -1:
        break

    # adds course mark to the list if it is a valid mark
    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print('That is not a valid mark, please try again.')

print('\nYour top six have a mean average of {}%'.format(markAvgMean(marks)))
print('Your top six have a median average of {}%'.format(markAvgMedian(marks)))