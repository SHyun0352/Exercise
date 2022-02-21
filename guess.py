#드디어 좀 간지나보이는 임포트?
import random

number = random.randint(1,10)

guess = int(input("Guess the number: "))

while guess != number:
    print("Wrong")
    guess = int(input("Try again: "))
print("You  got  it!")
