# ==========================================================
# Question 1: Find Duplicate Elements in a List
# ==========================================================

print("=" * 60)
print("Question 1: Find Duplicate Elements in a List")
print("=" * 60)

numbers = [1, 2, 3, 4, 2, 5, 1, 6]

seen = []
duplicates = []

for num in numbers:

    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)

duplicates.sort()

print("Original List :", numbers)
print("Duplicate Elements :", duplicates)


# ==========================================================
# Question 2: Find the Longest Word in a String
# ==========================================================

print("\n" + "=" * 60)
print("Question 2: Find the Longest Word in a String")
print("=" * 60)

sentence = "Python is a powerful programming language"

words = sentence.split()

longest_word = words[0]

for word in words:

    if len(word) > len(longest_word):
        longest_word = word

print("Sentence :", sentence)
print("Longest Word :", longest_word)


# ==========================================================
# Question 3: Find the Intersection of Two Lists
# ==========================================================

print("\n" + "=" * 60)
print("Question 3: Find the Intersection of Two Lists")
print("=" * 60)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = []

for num in list1:

    if num in list2:
        intersection.append(num)

print("List 1 :", list1)
print("List 2 :", list2)
print("Intersection :", intersection)


# ==========================================================
# Question 4: Merge Two Sorted Lists
# ==========================================================

print("\n" + "=" * 60)
print("Question 4: Merge Two Sorted Lists")
print("=" * 60)

list1 = [1, 3, 5]
list2 = [2, 4, 6]

merged = []

i = 0
j = 0

while i < len(list1) and j < len(list2):

    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1

    else:
        merged.append(list2[j])
        j += 1

# Add remaining elements from List1
while i < len(list1):
    merged.append(list1[i])
    i += 1

# Add remaining elements from List2
while j < len(list2):
    merged.append(list2[j])
    j += 1

print("List 1 :", list1)
print("List 2 :", list2)
print("Merged List :", merged)