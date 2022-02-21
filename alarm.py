day = int(input("1 Monday ... 7 Sunday: "))

if day <= 5:
    print("Alarm rings at 7")
elif day == 6:
    print("Alarm rings at 8")
else:
    print("Alarm rings at 9")
