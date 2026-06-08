# Take marks as input
marks = int(input("Enter marks (0-100): "))

# Grade Classification
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B+")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")