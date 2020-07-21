# TO-DO: complete the helper function below to merge 2 sorted arrays
import math


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    for i in range(0, len(merged_arr)):
        if i < len(arrA):
            merged_arr[i] = arrA[i]
        else:
            merged_arr[i] = arrB[i - len(arrA)]
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    mid = math.ceil(len(arr) / 2)
    if len(arr) == 1:
        return arr
    a = merge_sort(arr[:mid])
    b = merge_sort(arr[mid:])
    i = 0
    j = 0
    result = []
    while i != len(a) or j != len(b):
        if i != len(a) and (j == len(b) or a[i] < b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result
    
    
     

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))
# # STRETCH: implement the recursive logic for merge sort in a way that doesn't
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists
# # or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
