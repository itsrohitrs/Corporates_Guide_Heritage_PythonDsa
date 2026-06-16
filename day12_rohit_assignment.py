# ==========================================
# WEEK 3 - DAY 12 ASSIGNMENT SOLUTIONS
# ==========================================

import time
import numpy as np

# ==========================================
# Q1. Basic Binary Search
# ==========================================

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("Q1:", binary_search(arr, 23))


# ==========================================
# Q2. Count Occurrences Using Binary Search
# ==========================================

def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)

    if first == -1:
        return 0

    return last - first + 1


arr = [1, 2, 2, 2, 3, 4]
print("Q2:", count_occurrences(arr, 2))


# ==========================================
# Q3. Recursive Binary Search
# ==========================================

def recursive_binary_search(arr, target, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)
    else:
        return recursive_binary_search(arr, target, low, mid - 1)


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("Q3:", recursive_binary_search(arr, 23, 0, len(arr) - 1))


# ==========================================
# Q4. Factorial & Sum of Digits
# ==========================================

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def digit_sum(n):

    if n < 10:
        return n

    return n % 10 + digit_sum(n // 10)


print("Q4 Factorial:", factorial(5))
print("Q4 Digit Sum:", digit_sum(1234))


# ==========================================
# Q5. Performance Comparison
# ==========================================

start = time.time()

lst = []
for i in range(100000):
    lst.append(i)

list_time = time.time() - start

start = time.time()

arr_np = np.arange(100000)

numpy_time = time.time() - start

print("Q5 List Time:", list_time)
print("Q5 NumPy Time:", numpy_time)


# ==========================================
# Q6. Pair Sum - Find All Pairs
# ==========================================

def pair_sum_all(arr, target):

    left = 0
    right = len(arr) - 1

    pairs = []

    while left < right:

        current_sum = arr[left] + arr[right]

        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return pairs


arr = [1, 2, 3, 4, 5, 6, 7]
print("Q6:", pair_sum_all(arr, 8))


# ==========================================
# Q7. Remove Duplicates In Place
# ==========================================

def remove_duplicates(arr):

    if not arr:
        return 0

    slow = 0

    for fast in range(1, len(arr)):

        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


arr = [1, 1, 2, 3, 3, 4]

new_length = remove_duplicates(arr)

print("Q7 Array:", arr[:new_length])
print("Q7 Length:", new_length)


# ==========================================
# Q8. Max Average Subarray
# ==========================================

def max_average_subarray(arr, k):

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):

        window_sum += arr[i]
        window_sum -= arr[i - k]

        max_sum = max(max_sum, window_sum)

    return max_sum / k


arr = [1, 12, -5, -6, 50, 3]

print("Q8:", max_average_subarray(arr, 4))


# ==========================================
# Q9. Longest Subarray Sum <= K
# ==========================================

def longest_subarray(arr, k):

    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):

        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


arr = [1, 2, 3, 4, 5]

print("Q9:", longest_subarray(arr, 9))


# ==========================================
# BONUS CHALLENGE
# Search in a 2D Matrix
# ==========================================

def search_matrix(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:

        if matrix[row][col] == target:
            return True

        elif matrix[row][col] > target:
            col -= 1

        else:
            row += 1

    return False


matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print("Bonus:", search_matrix(matrix, 5))