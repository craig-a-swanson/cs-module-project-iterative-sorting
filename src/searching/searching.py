def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
import math
def binary_search(arr, target):

    # Get the length of the list and find the midpoint index
    # Test if the midpoint equals the target
    # Test if the target is greater than or less than the midpoint
    # If greater than, find the new midpoint between the current location and the end
    # If less than, find the new midpoint between the current location and the start
    # Keep going until we find the target, reach the end/start, no new elements to check.

    if len(arr) == 0:
        return -1
    max_iterations = math.log2(len(arr))
    midpoint = 0
    right_bound = len(arr) - 1
    left_bound = 0
    result = -1
    for iteration in range(1, math.floor(max_iterations) + 1): # find formula for maximum iterations in binary search
        midpoint = (right_bound - left_bound) // 2
        if arr[midpoint] == target:
            result = midpoint
            break
        elif arr[midpoint] > target:
            right_bound = midpoint
            
        elif arr[midpoint] < target:
            left_bound = midpoint
            
        

    return result  # not found
