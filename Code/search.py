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
    # Weird edge case where nothing was found
    if index >= len(array):
        return None
    # Found dart
    if item == array[index]:
        return index
    # Otherwise, loop again
    else:
        return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    min = 0
    max = len(array) - 1
    dart = (max + min) // 2
    while max >= min:
        dart = (max + min) // 2
        if item > array[dart]:
            min = dart + 1
        elif item < array[dart]:
            max = dart - 1
        else:
            return dart
    
    return None

def binary_search_recursive(array, item, left=None, right=None):
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests