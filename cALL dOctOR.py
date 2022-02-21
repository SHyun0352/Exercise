age = int(input("What is your age? "))
temp = int(input("What is the temperature? (Celcius) "))

if age < 2:
    if temp >= 38:
        print("Call a doctor.")
if temp > 39.5:
    print("High Fever")
