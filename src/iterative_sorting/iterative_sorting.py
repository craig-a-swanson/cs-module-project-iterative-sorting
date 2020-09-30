# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for cur_index in range(0, len(arr) - 1):
        smallest_index = cur_index
        # Iterate through to find the smallest value
        # Place it at the left-most boundary, swapping that element
        # Move the "boundary" from the left to right via nested loop
        for sub_index in range(cur_index, len(arr)):
            if arr[sub_index] < arr[smallest_index]:
                smallest_index = sub_index
        # Python swap code found online:
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


def bubble_sort(arr):
    changes = 1
    while changes > 0:
        changes = 0
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                placeholder = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = placeholder
                changes += 1
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # if the list is empty, return it
    if len(arr) == 0:
        return arr

    # if a value is not present for the maximum parameter, set it ourself
    if maximum is None:
        maximum = max(arr)

    # initialize list of zeroes
    working_list = [0] * (maximum + 1)

    # initialize an empty array for the final sorted list
    sorted_list = []

    # loop through arr:
    # use each value of arr as the index for the working_list
    # increment the value of that index in the working_list
    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        working_list[value] += 1
    
    # convert the working_list into the sorted_list:
    # loop through the working_list, skipping all the zero values
    # if a value exists > 0, append that index number to the sorted_list
    for index, value in enumerate(working_list):
        if value > 0:
            sorted_list.append(index)

    return sorted_list
