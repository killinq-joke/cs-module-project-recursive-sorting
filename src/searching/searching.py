# TO-DO: Implement a recursive implementation of binary search
import math


def binary_search(arr, target, start, end):
    # Your code here
    if start >= end:
        return -1
    mid = math.ceil((end + start) / 2)
    if arr[mid] == target:
        return mid
    elif end == 1:
        return binary_search(arr, target, start, 0)
    elif start == 1:
        return binary_search(arr, target, 0, end)
    
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid)
    elif arr[mid] < target:
        return binary_search(arr, target, mid, end)


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, 0, 0, len(arr1)-1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


# def agnostic_binary_search(arr, target):
#     # Your code here
