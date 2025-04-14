import random
print("welcome to the guess the number game")
print("you have 5 attempts to guess the number")
print("the number is between 1 and 100")
number = random.randint(1, 100)
attempts = 0
while attempts < 5:
    guess = int(input("guess the number: "))
    if guess == number:
        print("you guessed the number , congratulations! :)")
        break
    elif guess < number:
        print(f"the number is higher than {guess}")
    else:
        print(f"the number is lower than {guess}")
    attempts += 1
    print (f"you have {5 - attempts} attempts left")
if attempts == 5:
    print(f"you have used all your attempts, the number was {number}")
    print ("hardluck :(")