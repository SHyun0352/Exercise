DONOR_AGE = 16
DONOR_WEIGHT = 50

age = int(input("What is your age? "))
weight = int(input("What is your weight? "))

if age >= DONOR_AGE and weight >= DONOR_WEIGHT:
    print("You can donate blood")
if age < DONOR_AGE:
    print("You are too young to donate blood")
if age >= DONOR_AGE and weight < DONOR_WEIGHT:
    print("You are too light to donate blood")
