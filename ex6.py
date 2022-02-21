import random

number = random.randint(1, 1000)

# print(number)

trial = 0

mode = ""

while mode != "E" and mode != "H":
    mode = input("Choose mode. E | H: ").upper()
    if mode == "E":
        availableTrials = 10
    elif mode == "H":
        availableTrials = 4
    else:
        print("This is not valid input.")

guess = int(input("Guess a number: "))

while guess != number and trial < availableTrials:
    trial += 1
    if trial == availableTrials:
        print("Too many trials")
    elif number > guess:
        print("That's too low")
        guess = int(input("Try again: "))
    elif number < guess:
        print("That's too high")
        guess = int(input("Try again: "))

# 섹스
if guess == number:
    print(f"You got it {trial} guesses.")







