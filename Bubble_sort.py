def bubble_sort(this_list):
    n = 0
    try:
        if this_list[n] > this_list[n+1]:
            this_list[n], this_list[n+1] = this_list[n+1], this_list[n]
            n += 1
            return bubble_sort(this_list)
        else:
            n += 1
            return bubble_sort(this_list)
    except IndexError:
        return this_list