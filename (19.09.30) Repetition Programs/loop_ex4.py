import re
while True:
    password = str(input("Enter a new password: "))
    if not re.search("[A-Z]", password):
        print("You need at least one capital!\n")
    elif not re.search("[0-9]", password):
        print("You need at least one numeric character!\n")
    elif re.search("[~!@#$%^&*()-+=?/|<>,.\[\]\{\}:;]", password):
        print("Your password can only contain numbers, letters, and underscores!\n")
    else:
        break