print ("Welcome to the Ontario Science Centre!\n")
sciCen = input("Are you going to be visiting the Science Centre Exhibitions today? ").capitalize()
imax = input("\nAre you going to be watching an IMAX film today? ").capitalize()

sciPrice = 0
imaxPrice = 0

# Science Centre Calculation
if sciCen == "Yes":
    membership = input("\nDo you have a membership? ").capitalize()
    if membership == "Yes":
        sciPrice = 0
    else:
        age = int(input("\nHow old are you? "))
        if age >= 18 and age < 65:
            studentID = input("\nDo you have a student ID? ").capitalize()
            if studentID == "Yes":
                sciPrice = 16
            else:
                sciPrice = 22
        else:
            if age < 3:
                sciPrice = 0
            elif age >= 3 and age < 13:
                sciPrice = 13
            else:
                sciPrice = 16
tPrice = sciPrice

# IMAX Calculation
if imax == "Yes":
    if sciCen == "No":
        age = int(input("\nHow old are you? "))
    elif membership == "Yes":
        age = int(input("\nHow old are you? "))
    if age > 2:
        imaxPrice = 9
    
tPrice = sciPrice + imaxPrice 
# Parking Calculation  
parking = input("\nDid you need parking? ").capitalize()
if parking == "Yes":
    tPrice = tPrice + 10
    
print ("\nYour total today will be $" + str(tPrice) + " CAD.")