grades = []
courses = []
for x in range(0,10):
    course = str(input("Enter the course: "))
    courses.append(course)    
    grade = int(input("Enter a grade: "))
    grades.append(grade)
    
n = 0
print("\nMarks: ")
for x in range(0,10):
    print(courses[n] + ": " + str(grades[n]))
    n += 1
   
print("\nGrades: " + str(grades))
grades.sort()
print("Ordered Grades: " + str(grades))
grades.sort(reverse=True)
print("Reverse Ordered Grades: " + str(grades)) 

listAvg = 1
for x in range(0,10):
    avg = grades.pop()
    listAvg = listAvg + avg
print("\nThe average mark is " + str(listAvg/10))