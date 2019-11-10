import random
guess = 0
ans = random.randint(1,100)
print("Guess a magic number between 1 and 100.")
while guess != ans:
    guess = int(input("Enter your guess: "))
    if guess > ans:
        print("Your guess is too high.\n")
    elif guess < ans:
        print ("Your guess is too low.\n")
ans = str(ans)
print("Yes, the number is " + ans + ".")