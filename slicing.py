# example=[1,2,3,4,5,6,7,8,9,10]
# print(example[2:5])
# print(example[:5])
# print(example[0:])
# print(example[5:10])
# print(example[::2])
# print(example[1:10:2])
# print(example[::-1])
# print(example[5:1:-1])
# print(example[5:0:-1])
# print(example[5:0:-2])


# ==============================================================
#                PYTHON LIST SLICING
# ==============================================================
#
# Definition:
# List slicing is a technique used to extract a portion (sub-list)
# from an existing list without modifying the original list.
#
# Syntax:
#
# list_name[start : stop : step]
#
# --------------------------------------------------------------
# Parameters:
#
# start
#   - Starting index (Inclusive)
#   - Default = 0
#
# stop
#   - Ending index (Exclusive)
#   - Default = Length of the list
#
# step
#   - Number of positions to move
#   - Default = 1
#   - Negative step means traverse backwards.
#
# --------------------------------------------------------------
# Important Rules:
#
# 1. Start index is INCLUDED.
# 2. Stop index is EXCLUDED.
# 3. Omitting start means begin from index 0.
# 4. Omitting stop means go till the end.
# 5. Omitting step means move one element at a time.
# 6. Negative step traverses the list in reverse order.
#
# ==============================================================

# Creating a list
example = [1,2,3,4,5,6,7,8,9,10]

# ==============================================================
# Index Representation
# ==============================================================

# Positive Index
#
# Value :  1   2   3   4   5   6   7   8   9   10
# Index :  0   1   2   3   4   5   6   7   8    9
#
# Negative Index
#
# Value :   1   2   3   4   5   6   7   8   9   10
# Index : -10 -9 -8 -7 -6 -5 -4 -3 -2  -1

# ==============================================================
# Example 1
# Extract elements from index 2 to index 4
#
# Start = 2 (Included)
# Stop = 5 (Excluded)
#
# Index : 0 1 [2 3 4] 5 6 7 8 9
# Value : 1 2 [3 4 5] 6 7 8 9 10
# ==============================================================

print(example[2:5])
# Output: [3, 4, 5]


# ==============================================================
# Example 2
# From beginning up to index 4
#
# Since start is omitted,
# Python assumes start = 0.
# ==============================================================

print(example[:5])
# Output: [1, 2, 3, 4, 5]


# ==============================================================
# Example 3
# From index 0 till the end
#
# Stop is omitted.
# Python automatically goes till the last element.
# ==============================================================

print(example[0:])
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ==============================================================
# Example 4
# Elements from index 5 till index 9
#
# Start = 5
# Stop = 10
# ==============================================================

print(example[5:10])
# Output: [6, 7, 8, 9, 10]


# ==============================================================
# Example 5
# Every second element
#
# Step = 2
#
# Python skips one element after every selection.
# ==============================================================

print(example[::2])
# Output: [1, 3, 5, 7, 9]


# ==============================================================
# Example 6
# Every second element starting from index 1
#
# Start = 1
# Stop = 10
# Step = 2
# ==============================================================

print(example[1:10:2])
# Output: [2, 4, 6, 8, 10]


# ==============================================================
# Example 7
# Reverse the complete list
#
# Step = -1
#
# Negative step means move backwards.
# ==============================================================

print(example[::-1])
# Output:
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# ==============================================================
# Example 8
# Reverse slice
#
# Start = Index 5 (Value = 6)
# Stop = Index 1 (Excluded)
# Step = -1
#
# Traversal:
#
# Index : 5 → 4 → 3 → 2
# Value : 6 → 5 → 4 → 3
# ==============================================================

print(example[5:1:-1])
# Output: [6, 5, 4, 3]


# ==============================================================
# Example 9
# Reverse slice
#
# Start = Index 5
# Stop = Index 0 (Excluded)
#
# Since stop is excluded,
# index 0 is NOT included.
#
# Traversal:
#
# 5 → 4 → 3 → 2 → 1
#
# ==============================================================

print(example[5:0:-1])
# Output:
# [6, 5, 4, 3, 2]


# ==============================================================
# Example 10
# Reverse traversal with step = -2
#
# Start = Index 5
# Stop = Index 0 (Excluded)
#
# Jump two positions backward.
#
# Traversal:
#
# Index : 5 → 3 → 1
# Value : 6 → 4 → 2
# ==============================================================

print(example[5:0:-2])
# Output:
# [6, 4, 2]


# ==============================================================
# Summary Table
# ==============================================================
#
# Expression         Meaning
# --------------------------------------------------------------
# list[a:b]          Elements from a to b-1
#
# list[:b]           Beginning to b-1
#
# list[a:]           a to end
#
# list[:]            Copy the complete list
#
# list[::2]          Every second element
#
# list[1::3]         Every third element from index 1
#
# list[::-1]         Reverse the entire list
#
# list[a:b:-1]       Reverse slice
#
# list[::-2]         Reverse list taking alternate elements
#
# ==============================================================

# Quick Revision
#
# ✔ Start index is Included.
# ✔ Stop index is Excluded.
# ✔ Default start = 0.
# ✔ Default stop = End of list.
# ✔ Default step = 1.
# ✔ Negative step traverses backward.
# ✔ Slicing never changes the original list.
# ✔ Slicing creates a new list.
#
# ==============================================================