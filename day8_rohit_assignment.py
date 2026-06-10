# File Name: day8_rohit_assignment.py

# ==========================================================
# Assignment — Section A: Lists
# ==========================================================

# ---------------- Question 1 ----------------

print("\n===== Question 1 =====")

student_marks = [78, 85, 92, 67, 88, 74, 95, 81, 69, 90]

print("First 3 Elements:", student_marks[:3])
print("Last 3 Elements:", student_marks[-3:])
print("Alternate Elements:", student_marks[::2])

print("Total Elements:", len(student_marks))

student_marks[4] = 95
print("Updated List:", student_marks)

print("Reverse Order:", student_marks[::-1])

# ---------------- Question 2 ----------------

print("\n===== Question 2 =====")

scores = [55, 72, 88, 43, 91, 67, 55, 76]

print("Count of 55:", scores.count(55))
print("Index of 88:", scores.index(88))

scores.append(80)
print("After Append:", scores)

scores.insert(3, 100)
print("After Insert:", scores)

scores.remove(55)
print("After Remove:", scores)

scores.sort()
print("Ascending:", scores)

scores.sort(reverse=True)
print("Descending:", scores)

popped = scores.pop()

print("Popped Value:", popped)
print("Remaining List:", scores)

# ---------------- Question 3 ----------------

print("\n===== Question 3 =====")

# a
squares = [x**2 for x in range(1, 16)]
print("Squares:", squares)

# b
evens = [x for x in range(1, 51) if x % 2 == 0]
print("Even Numbers:", evens)

# c
words = ['hello', 'world', 'python', 'is', 'great']

long_words = [word for word in words if len(word) > 4]

print("Words > 4 chars:", long_words)

# d
matrix = [[1,2,3],[4,5,6],[7,8,9]]

flat = [num for row in matrix for num in row]

print("Flattened List:", flat)

# e
pairs = [(x, x**2) for x in range(1,9)]

print("Number-Square Tuples:", pairs)

# ==========================================================
# Assignment — Section B: Tuples
# ==========================================================

# ---------------- Question 4 ----------------

print("\n===== Question 4 =====")

months = (
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
)

print("3rd Month:", months[2])
print("Last Month:", months[-1])
print("Months Index 3-6:", months[3:7])

# Tuple is immutable
# months[0] = "January_New"

name = ("Rohit",)

print("Single Element Tuple:", name)
print("Type:", type(name))

months_list = list(months)

months_list.append("Intercalary")

months = tuple(months_list)

print("Updated Months Tuple:")
print(months)

# ---------------- Question 5 ----------------

print("\n===== Question 5 =====")

employee = (
    "Rajesh Kumar",
    34,
    "Data Analyst",
    75000,
    "Bangalore"
)

name, age, job, salary, city = employee

print("Name:", name)
print("Age:", age)
print("Job:", job)
print("Salary:", salary)
print("City:", city)

first, *middle, second_last, last = employee

print("First:", first)
print("Middle:", middle)
print("Second Last:", second_last)
print("Last:", last)

x = 10
y = 20
z = 30

x, y, z = z, x, y

print("Swapped:", x, y, z)

data = [
    ("Alice",90),
    ("Bob",85),
    ("Charlie",78),
    ("Diana",92)
]

for name, marks in data:
    print(f"{name} scored {marks}/100")

def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([10,20,30,40,50])

print("Minimum:", minimum)
print("Maximum:", maximum)

# ==========================================================
# Assignment — Section C: Iteration
# ==========================================================

# ---------------- Question 6 ----------------

print("\n===== Question 6 =====")

temperatures = [22,35,18,40,28,15,33,27]

print("\nTemperatures with Index:")

for index, temp in enumerate(temperatures):
    print(index, temp)

count = 0

for temp in temperatures:
    if temp > 30:
        count += 1

print("Above 30:", count)

names = ["Alice","Bob","Charlie"]
marks = [85,92,78]

print("\nUsing Zip:")

for name, mark in zip(names, marks):
    print(name, mark)

temp_list = temperatures.copy()

i = 0

while i < len(temp_list):

    if temp_list[i] <= 25:
        temp_list.pop(i)
        print(temp_list)

    else:
        i += 1

print("\nMultiplication Table Grid")

for i in range(1,6):

    for j in range(1,6):
        print(f"{i*j:3}", end=" ")

    print()

# ==========================================================
# Challenge 1 — Student Grade System
# ==========================================================

print("\n===== Challenge 1 =====")

students = [
    ("Alice",101,[80,85,90,88,92]),
    ("Bob",102,[70,75,80,72,78]),
    ("Charlie",103,[90,91,89,95,94]),
    ("Diana",104,[60,65,70,68,72]),
    ("Eve",105,[85,86,87,88,89]),
    ("Frank",106,[50,55,58,60,62]),
    ("Grace",107,[95,96,97,98,99]),
    ("Harry",108,[72,74,76,78,80]),
    ("Ivy",109,[65,67,69,71,73]),
    ("Jack",110,[88,90,92,91,89])
]

def calculate_average(marks):
    return sum(marks) / len(marks)

averages = [
    (name, calculate_average(marks))
    for name, roll, marks in students
]

averages.sort(key=lambda x: x[1], reverse=True)

print("\nClass Rank")

rank = 1

for name, avg in averages:
    print(rank, name, round(avg,2))
    rank += 1

count_above_75 = len(
    [avg for name, avg in averages if avg > 75]
)

print("\nStudents Above 75 Average:", count_above_75)

topper = max(averages, key=lambda x: x[1])

lowest = min(averages, key=lambda x: x[1])

print("Topper:", topper)

print("Lowest Average:", lowest)

# ==========================================================
# Challenge 2 — Inventory Management
# ==========================================================

print("\n===== Challenge 2 =====")

products = [
    (101,"Mouse",500,10),
    (102,"Keyboard",1200,5),
    (103,"Monitor",8000,2),
    (104,"Printer",6000,4),
    (105,"Speaker",2500,8),
    (106,"Webcam",1800,3),
    (107,"SSD",3500,6),
    (108,"Laptop",55000,2)
]

def add_product(product):
    products.append(product)

def remove_product(name):

    for product in products:

        if product[1].lower() == name.lower():
            products.remove(product)
            break

def update_quantity(name, qty):

    for i in range(len(products)):

        if products[i][1].lower() == name.lower():

            pid, pname, price, old_qty = products[i]

            products[i] = (pid, pname, price, qty)

            break

def total_inventory_value():

    total = 0

    for pid, name, price, qty in products:
        total += price * qty

    return total

print("\nInventory Value:", total_inventory_value())

print("\nLow Stock Products")

for product in products:

    if product[3] < 5:
        print(product)

print("\nProducts Sorted by Price")

sorted_products = sorted(products, key=lambda x: x[2])

for product in sorted_products:
    print(product)

search = "Monitor"

print("\nSearch Result")

for product in products:

    if product[1].lower() == search.lower():

        print(product)

        break

print("\n===== Assignment Completed Successfully =====")