def linear_search(l_nrs, target_x, idx=0):
    try:
        assert all(type(item) == int for item in l_nrs) is True
    except AssertionError:
        print('There is an invalid item in the list')
    else:
        if len(l_nrs) > 0:
            if all(type(item) == int for item in l_nrs) is True:
                if target_x >= 0:
                    if idx >= 0:
                        if l_nrs[idx] == target_x:
                            return True
        return False
