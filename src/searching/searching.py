# TO-DO: Implement a recursive implementation of binary search
import math


def binary_search(arr, target, start, end):
    # Your code here
    if start == end:
        return -1
    if end == 1:
        end = 0
    mid = math.ceil(end / 2)
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid)
    else:
        return binary_search(arr, target, mid, end)
    return -1

arr1 = [-8, 2, 6]
print(binary_search(arr1, -8, 0, len(arr1)-1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


# def agnostic_binary_search(arr, target):
#     # Your code here
