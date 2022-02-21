number_of_numbers = int(input("How  many numbers to be averaged? "))

count = 0

total = 0

while count < number_of_numbers:
    count += 1
    number = int(input(f"Enter number {count}: "))
    total += number

print(f"Total is {total}")

print(f"Average is {total / number_of_numbers}")














