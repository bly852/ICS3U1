def palindrome(string):
    #Takes in a string and outputs a boolean value for whether the string is a palindrome or not
    if str(string) == str(string)[::-1]:
        return True
    else:
        return False

print(palindrome('racecar'))