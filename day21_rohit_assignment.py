# ==========================================================
# Program 1: Reverse a String (Without Using Built-in Functions)
# ==========================================================

def reverse_string(s):
    rev = ""

    for ch in s:
        rev = ch + rev

    return rev


text = "Python"

print("=" * 50)
print("Program 1: Reverse a String")
print("Original String :", text)
print("Reversed String :", reverse_string(text))


# ==========================================================
# Program 2: Check if a String is a Palindrome
# ==========================================================

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


text = "madam"

print("\n" + "=" * 50)
print("Program 2: Palindrome Check")

if is_palindrome(text):
    print(text, "is a Palindrome")
else:
    print(text, "is Not a Palindrome")


# ==========================================================
# Program 3: Remove Duplicate Elements from a List
# ==========================================================

def remove_duplicates(arr):
    result = []

    for item in arr:
        if item not in result:
            result.append(item)

    return result


numbers = [1, 2, 3, 2, 4, 1, 5, 3]

print("\n" + "=" * 50)
print("Program 3: Remove Duplicates")
print("Original List :", numbers)
print("After Removing Duplicates :", remove_duplicates(numbers))


# ==========================================================
# Program 4: Find the Factorial of a Number
# ==========================================================

print("\n" + "=" * 50)
print("Program 4: Factorial")

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")

elif num == 0 or num == 1:
    print("Factorial =", 1)

else:
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("Factorial =", factorial)


# ==========================================================
# Program 5: Find the Largest Element in a List
# ==========================================================

numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("\n" + "=" * 50)
print("Program 5: Largest Element")
print("List :", numbers)
print("Largest Element :", largest)


# ==========================================================
# Program 6: Check if a Number is Prime
# ==========================================================

print("\n" + "=" * 50)
print("Program 6: Prime Number")

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime Number")

else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is not a Prime Number")