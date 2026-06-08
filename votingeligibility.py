age = int(input("Enter age: "))
is_citizen = True
is_registered = True

if age >= 18 and is_citizen and is_registered:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")