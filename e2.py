# 응애나애기
age = int(input("What is the patient's age? "))

# 쪼매  귀찮
if age < 12:
    weight = int(input("What is the patient's weight? (in kg) "))
    dose = weight * 10
else:
    dose = 1000

# 그냥 주석
print(f"Recommend {dose} mg paracetamol")
