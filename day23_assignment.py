# ==========================================================
# Question 1: Reverse an Array/List
# ==========================================================

print("=" * 60)
print("Question 1: Reverse an Array/List")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original List :", numbers)
print("Reversed List :", reversed_list)


# ==========================================================
# Question 2: Find the Largest and Smallest Element
# ==========================================================

print("\n" + "=" * 60)
print("Question 2: Find the Largest and Smallest Element")
print("=" * 60)

numbers = [12, 45, 7, 89, 23]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("List :", numbers)
print("Largest =", largest)
print("Smallest =", smallest)


# ==========================================================
# Question 3: Remove Duplicate Elements
# ==========================================================

print("\n" + "=" * 60)
print("Question 3: Remove Duplicate Elements")
print("=" * 60)

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_list = []

for num in numbers:

    if num not in unique_list:
        unique_list.append(num)

print("Original List :", numbers)
print("List after Removing Duplicates :", unique_list)


# ==========================================================
# Question 4: Count Frequency of Each Element
# ==========================================================

print("\n" + "=" * 60)
print("Question 4: Count Frequency of Each Element")
print("=" * 60)

numbers = [1, 2, 2, 3, 1, 4, 2]

frequency = {}

for num in numbers:

    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("List :", numbers)
print("\nFrequency of Each Element:")

for key, value in frequency.items():
    print(key, "->", value)


# ==========================================================
# Question 5: Find the Second Largest Number
# ==========================================================

print("\n" + "=" * 60)
print("Question 5: Find the Second Largest Number")
print("=" * 60)

numbers = [15, 10, 45, 32, 60]

largest = numbers[0]
second_largest = numbers[0]

# Find the largest element
for num in numbers:
    if num > largest:
        largest = num

# Find the second largest element
for num in numbers:
    if num > second_largest and num != largest:
        second_largest = num

print("List :", numbers)
print("Largest =", largest)
print("Second Largest =", second_largest)