def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1           


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    return -1

arr = [10, 20, 30, 40, 50, 60, 70]
target = 40

print("Array:", arr)
print("Linear Search:", linear_search(arr, target))
print("Binary Search (Iterative):", binary_search(arr, target))
print("Binary Search (Recursive):", binary_search_recursive(arr, target, 0, len(arr)-1))
