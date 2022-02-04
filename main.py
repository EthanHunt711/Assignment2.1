from binary_search import binary_search
from linear_search import linear_search
from bubble_sort import bubble_sort
from get_random import lists
import time


"""The main program for implementing the algorithms and saving the running time"""
if __name__ == "__main__":
    something_start = time.time()
    something_l = linear_search(lists[0], 5, 5)
    something_stop = time.time()
    something_running_time_linear = something_stop - something_start

    something_start = time.time()
    something_b = binary_search(sorted(lists[0]), 5)
    something_stop = time.time()
    something_running_time_binary = something_stop - something_start

    print(f'The running time for Linear Search is: {something_running_time_linear}')
    print(f'The serach result is: {something_l}')
    print('---------------------------------------------------------------------------')
    print(f'The running time for Binary Search is: {something_running_time_binary}')
    print(f'The search result is: {something_b}')
