
# Question 1: Find the Second Largest Number

print("=" * 60)
print("Question 1: Find the Second Largest Number")
print("=" * 60)

n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("Second Largest = -1")
else:
    print("Second Largest =", second)


# Question 2: Word Frequency Counter

print("\n" + "=" * 60)
print("Question 2: Word Frequency Counter")
print("=" * 60)

sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")

for word in frequency:
    print(word, frequency[word])

# Question 3: Student Record Analyzer

print("\n" + "=" * 60)
print("Question 3: Student Record Analyzer")
print("=" * 60)

n = int(input("Enter the number of students: "))
students = []
total = 0

for i in range(n):
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    students.append((name, marks))
    total += marks

average = total / n
result = []

for name, marks in students:
    if marks >= average:
        result.append(name)

result.sort()
print("\nStudents scoring greater than or equal to average:")

for name in result:
    print(name)

# Question 4: Remove Duplicate Elements

print("\n" + "=" * 60)
print("Question 4: Remove Duplicate Elements")
print("=" * 60)

n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("\nList after removing duplicates:")
print(*unique)


# Question 5: Employee Performance Ranking


print("\n" + "=" * 60)
print("Question 5: Employee Performance Ranking")
print("=" * 60)

n = int(input("Enter the number of employees: "))
emp = []

for i in range(n):
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    score = int(input("Enter Employee Score: "))
    emp.append((employee_id, name, score))

highest = emp[0]

for e in emp:
    if e[2] > highest[2]:
        highest = e

    elif e[2] == highest[2]:
        if e[1] < highest[1]:
            highest = e

print("\nTop Employee:")
print(highest[1], highest[2])