# Merge Sort algorithm taken from:
# https://www.geeksforgeeks.org/merge-sort/
# acessed on 9/23/24
# License: none given
# author: none given
####
# CHANGELOG:
# - added "return arr" to end of "def merge_sort(arr, left, right):" function
#       - line 74
# - added lru_cache decorator to merge_sort(arr, left, right): for an upgrade in effiency
#       - line 66
# - added "arr = list(arr)" since the merge(arr, left, mid, right): requires indexing 
#       - line 23
####
# python 3 implementation of Recursive Merge Sort
# This function handles the merge sort algorithm.
# start and end points to the starting point and ending point 
# that undergo the sorting process. 

from functools import lru_cache

def merge(arr, left, mid, right):
    arr = list(arr)
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

@lru_cache()
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print_list(arr)

    merge_sort(arr, 0, len(arr) - 1)

    print("\nSorted array is")
    print_list(arr)