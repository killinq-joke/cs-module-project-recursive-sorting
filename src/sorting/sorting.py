# TO-DO: complete the helper function below to merge 2 sorted arrays
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


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge(arr1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

# TO-DO: implement the Merge Sort function below recursively


# def merge_sort(arr):
#     # Your code here

#     return arr

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists
# # or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
