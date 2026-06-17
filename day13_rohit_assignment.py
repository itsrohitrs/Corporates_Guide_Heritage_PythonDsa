# ==========================================
# ASSIGNMENT: SORTING ALGORITHMS
# ==========================================

# ==========================================
# Q1. Bubble Sort – Trace the Steps
# ==========================================

print("========== Q1: Bubble Sort ==========")

arr = [29, 10, 14, 37, 13]
n = len(arr)

for i in range(n - 1):
    swapped = False

    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    print(f"Pass {i + 1}: {arr}")

    if not swapped:
        break

print("Sorted Array:", arr)
print("Passes Required:", i + 1)


# ==========================================
# Q2. Selection Sort
# ==========================================

print("\n========== Q2: Selection Sort ==========")

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Step {i + 1}: {arr}")

    return arr


arr = [64, 25, 12, 22, 11, 90, 3]

print("Original Array:", arr)
selection_sort(arr)

print("\nMinimum number of swaps:")
print("0 swaps (when array is already sorted).")
print("Reason: Every element is already in correct position.")


# ==========================================
# Q3. Insertion Sort – Best vs Worst Case
# ==========================================

print("\n========== Q3: Insertion Sort ==========")

# Part A
arr1 = [3, 5, 7, 9, 11]
comparisons_best = 0

for i in range(1, len(arr1)):
    key = arr1[i]
    j = i - 1

    comparisons_best += 1

    while j >= 0 and arr1[j] > key:
        comparisons_best += 1
        arr1[j + 1] = arr1[j]
        j -= 1

    arr1[j + 1] = key

print("Best Case Array:", arr1)
print("Comparisons:", comparisons_best)

# Part B
arr2 = [11, 9, 7, 5, 3]
comparisons_worst = 0

for i in range(1, len(arr2)):
    key = arr2[i]
    j = i - 1

    while j >= 0:
        comparisons_worst += 1

        if arr2[j] > key:
            arr2[j + 1] = arr2[j]
            j -= 1
        else:
            break

    arr2[j + 1] = key

print("\nWorst Case Array:", arr2)
print("Comparisons:", comparisons_worst)

print("\nObservation:")
print("Best Case  -> O(n)")
print("Worst Case -> O(n²)")


# ==========================================
# Q4. Merge Sort – Recursion Tree
# ==========================================

print("\n========== Q4: Merge Sort ==========")

print("Recursion Tree:")

print("[8,3,5,4,2,7,1,6]")
print("├── [8,3,5,4]")
print("│   ├── [8,3]")
print("│   │   ├── [8]")
print("│   │   └── [3]")
print("│   └── [5,4]")
print("│       ├── [5]")
print("│       └── [4]")
print("└── [2,7,1,6]")
print("    ├── [2,7]")
print("    │   ├── [2]")
print("    │   └── [7]")
print("    └── [1,6]")
print("        ├── [1]")
print("        └── [6]")

print("\nMerge Steps:")

print("[8] + [3] -> [3,8]")
print("[5] + [4] -> [4,5]")
print("[3,8] + [4,5] -> [3,4,5,8]")

print("[2] + [7] -> [2,7]")
print("[1] + [6] -> [1,6]")
print("[2,7] + [1,6] -> [1,2,6,7]")

print("[3,4,5,8] + [1,2,6,7] -> [1,2,3,4,5,6,7,8]")


# ==========================================
# Q5. Quick Sort – Pivot Selection
# ==========================================

print("\n========== Q5: Quick Sort ==========")

arr = [15, 3, 9, 8, 5, 2, 7, 1, 6]

print("Original Array:", arr)

pivot = arr[-1]

i = -1

for j in range(len(arr) - 1):

    if arr[j] <= pivot:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]

arr[i + 1], arr[-1] = arr[-1], arr[i + 1]

print("Pivot:", pivot)
print("After One Partition:", arr)

print("\nWorst Case of Quick Sort:")
print("Occurs when pivot always becomes smallest or largest element.")
print("Example:")
print("[1,2,3,4,5,6,7,8]")
print("or")
print("[8,7,6,5,4,3,2,1]")

print("\nComplexity:")
print("Best/Average Case -> O(n log n)")
print("Worst Case -> O(n²)")

print("\nHow to Avoid?")
print("1. Random Pivot")
print("2. Median-of-Three Pivot")
print("3. Use Randomized Quick Sort")