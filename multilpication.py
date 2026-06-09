n = int(input("enter a number"))
print(f"\nMultiplication Table of {n}")

for i in range(1,13):
    print(f"{n} x {i:2} = {n * i:3}")