#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def clean_text(text):
    clean = " ?!,.;:-_'"
    for char in clean:
        text = text.replace(char, "")
    return text

def is_palindrome_iterative(text):
    # Time Complexity: O(n) because we use a loop to iterate
    clean_text(text)

    start = 0
    end = len(text) - 1
    
    if len(text) < 1:
        return True
    
    while start <= end:
        if text[start].lower() != text[end].lower():
            return False
        start += 1
        end -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # Time Complexity: O(n)
    if left == None:
        left = 0
        right = len(text) - 1

    clean_text(text)
    
    if len(text) < 1:
        return True
    if left <= right and right <= len(text) - 1:
        if text[left].lower() != text[right].lower():
            return False
        is_palindrome_recursive(text, left+1, right-1)
    return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
