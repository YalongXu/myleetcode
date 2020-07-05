import random


def binary_search(array: list, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


###############
aList = list(range(10))
for i in range(10):
    print("index of target %d:" % i)
    print(binary_search(list(range(10)), i))


