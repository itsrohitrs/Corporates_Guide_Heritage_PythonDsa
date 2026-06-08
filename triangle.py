# Input three sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check Triangle Inequality (short-circuit with and)
if a + b > c and a + c > b and b + c > a:

    print("Valid Triangle")

    # Check Triangle Type
    if a == b == c:
        print("Type: Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Type: Isosceles Triangle")

    else:
        print("Type: Scalene Triangle")

    # Check Right-Angled Triangle
    sides = sorted([a, b, c])

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("Also a Right-Angled Triangle")

else:
    print("Invalid Triangle")