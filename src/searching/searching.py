# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    l = end - start
    m = start + l//2
    if end < start:
        return -1
    return m if target == arr[m] else (
    binary_search(arr,
                  target,
                  start * (target < arr[m]) + m * (target > arr[m]),
                  end * (target > arr[m]) + m * (target < arr[m])))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target, start=0, end=None, ascending=None):
# Your code here
    if end is None:
        end = len(arr) - 1
        ascending = arr[start] < arr[end]
    l = end - start
    m = start + l//2
    if end < start:
        return -1
    l = ascending ^ (target < arr[m])
    n = not l
    return m if target == arr[m] else (
    agnostic_binary_search(arr,
                  target,
                  start * n + (m + 1) * l,
                  (m - 1) * n + end * l, ascending))
