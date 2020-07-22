# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    arr = []
    a = b = 0
    while a < len(arrA) and b < len(arrB):
        l = arrA[a] < arrB[b]
        n = not l
        arr.append(arrA[a] * l + arrB[b] * n)
        a += l
        b += n
    arr.extend(arrA[a:])
    arr.extend(arrB[b:])
    return arr

# TO-DO: implement the Merge Sort function below recursively
merge_sort = lambda arr : arr if len(arr) <= 1 else merge(
                                                        merge_sort(
                                                            arr[:len(arr)//2]
                                                        ),
                                                        merge_sort(
                                                            arr[len(arr)//2:]
                                                        )
                                                    )

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    if arr[start] > arr[end]:
        arr[start:mid], arr[mid:end] = arr[mid:end], arr[start:mid]
# "This is also a lot faster (4x) than most of the other solutions,
# for 100k elements on my Core2Duo with Python2.7 (Ubuntu15.10 x86-64).
# It doesn't make any mmap/munmap system calls while running,
# so it's actually swapping in-place instead of making the interpreter
# allocate and free scratch memory."
#       - a random stack overflow comment from 2016 so maybe it's still true lol

merge_sort_in_place = lambda arr, l, r : arr if r - l <= 1 else merge_in_place(
                                                                    merge_sort_in_place(
                                                                        arr,
                                                                        l,
                                                                        (l + r) // 2
                                                                    ),
                                                                    merge_sort_in_place(
                                                                        arr,
                                                                        (l + r) // 2,
                                                                        r
                                                                    )
                                                                )
