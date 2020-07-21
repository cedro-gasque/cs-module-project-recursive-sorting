# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, *args):
    # Your code here
    l = len(arr)
    m = l//2
    if l == 0:
        return -1
    elif target == arr[m]:
        return m
    elif target < arr[m]:
        return binary_search(arr[:m], target)
    elif target > arr[m]:
        r = binary_search(arr[m:], target)
        return r + m * (r >= 0)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
