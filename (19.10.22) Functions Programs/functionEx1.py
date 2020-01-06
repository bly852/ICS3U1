def palindrome(string):
    """palindrome (string) - returns a boolean value for whether the parameter string is a palindrome"""
    if str(string) == str(string)[::-1]:
        return True
    else:
        return False


print(palindrome('racecar'))
