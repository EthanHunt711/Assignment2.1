def bubble_sort(this_list):
    swap = True
    for i in range(len(this_list)-1):
        if this_list[i] > this_list[i+1]:
            this_list[i], this_list[i+1] = this_list[i+1], this_list[i]
            swap = False
    if swap:
        return this_list
    return bubble_sort(this_list)
