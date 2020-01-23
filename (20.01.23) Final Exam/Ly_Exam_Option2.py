def mark_counter(marks, min, max):
    """
    mark_counter (marks, min, max) - takes in a list of marks and returns a list with the number of marks in between the
    range(inclusive) represented by a '*'
    """
    counter = 0
    for mark in marks:
        if min <= mark <= max:
            counter += 1
    return counter

# list to store all marks
marks = []

# infinite loop
while True:
    # grab input from the user
    mark = int(input('\nEnter a mark: '))
    # break out of the loop when -1 is entered
    if mark == -1:
        break
    # add mark to the marks list if a valid mark, otherwise user is asked to try again
    elif 0 <= mark <= 100:
        marks.append(mark)
    else:
        print('That is not a valid mark please try again.')

# prints out the histogram to the console
print('\n0 - 49   : {}'.format('*' * (mark_counter(marks, 0, 49))))
print('50 - 59  : {}'.format('*' * (mark_counter(marks, 50, 59))))
print('60 - 69  : {}'.format('*' * (mark_counter(marks, 60, 69))))
print('70 - 79  : {}'.format('*' * (mark_counter(marks, 70, 79))))
print('80 - 100 : {}'.format('*' * (mark_counter(marks, 80, 100))))
print('Average (Mean) {}%'.format(sum(marks)//len(marks)))
