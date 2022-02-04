def binary_search(l_sorted, target_x):
    """This function takes two parameters: a sorted list
    and a target value"""
    try:
        assert l_sorted == sorted(l_sorted)  # check if the list is sorted which is a requirement
    except AssertionError:
        print('The input list is not sorted')  # handling the unsorted list error
    else:
        n = len(l_sorted)
        left = 0  # the left bound
        right = n-1  # the right bound
        while left <= right:  # checking whether the left and right bound collide
            middle = (left + right) // 2  # dividing the list for faster searching
            if target_x < l_sorted[middle]:  # if the target value is in the left half
                right = middle-1  # alter the right bound
            elif target_x > l_sorted[middle]:  # if the target value is in the right half
                left = middle+1  # alter the left bound
            else:
                return True  # if the target value is in the list
        return False   # if the target value is not in the list
