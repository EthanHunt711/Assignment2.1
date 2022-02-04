def binary_search(l_sorted, target_x):
    try:
        assert l_sorted == sorted(l_sorted)
    except AssertionError:
        print('The input list is not sorted')
    else:
        n = len(l_sorted)
        left = 0
        right = n-1
        while left <= right:
            middle = (left + right) // 2
            if target_x < l_sorted[middle]:
                right = middle-1
            elif target_x > l_sorted[middle]:
                left = middle+1
            else:
                return True
        return False
