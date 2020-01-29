#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return None
    
    if item == array[index]:
        return index
    
    else:
        return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    half_array = int(len(array)/2)
    # Start at the beginning of the step
    start = array[half_array]
    
    # How to loop this?
    for _ in range(half_array):
        # if it's smaller than the target, cut the array search in half choose the top one
        if array.index(start) < array.index(item):
            start = array[start:]
        # if it's bigger go down
        if array.index(start) > array.index(item):
            start = array[:start]
        else:
            return item

def binary_search_recursive(array, item, left=None, right=None):
    halfway = len(array)/2
    # this total determines how many times the array was split
    total = left + right
    array_slice = len(array)/(total+1)
    
    
    if array.index(halfway) < array.index(item):
        
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
