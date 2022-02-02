def search(arr, i):
    n = len(arr)
    left = 0
    right = n-1
    while left <= right:
        middle = (left + right) // 2
        if i < arr[middle]:
            right = middle-1
        elif i > arr[middle]:
            left = middle+1
        else:
            return middle
    return -1