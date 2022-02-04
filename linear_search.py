def linear_search(l_nrs, target_x, idx=0):
    """This function takes three parameters: a list of numbers,
        a target value, and an index number"""
    try:  # checking whether the list contains only integers
        assert all(type(item) == int for item in l_nrs) is True  # it could be altered so the list contains floats
    except AssertionError:
        print('There is an invalid item in the list')
    else:
        if len(l_nrs) > 0:  # the list is not empty
            if idx >= 0 <= (len(l_nrs)-1):  # if the given index is not a negative number or out of range
                if l_nrs[idx] == target_x:  # if the targeted value is within the list
                    return True
        return False
