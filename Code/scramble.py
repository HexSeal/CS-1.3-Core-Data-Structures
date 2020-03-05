# sort by length
# Only include words that have a first letter that's present in the scramble
# Double letter check
# Binary Search the tree created

from binarytree import BinarySearchTree
import os

# Get the word list from the OS, then split it
f = open('/usr/share/dict/words', 'r')
wordList = f.read().splitlines()
tree = BinarySearchTree(wordList)

# Helper methods to narrow search and lower runtime.
def firstLetter(word, tree):
    """Cut the amount of words in the dictionaryTree down to only words who's first letter is present in the scrambled word"""
    splitWord = str.split(word)

    for words in tree.items_pre_order:
        for letter in splitWord:
            if letter == words[0]:
                tree.append(word)
    return tree


def doubleLetter(word, dictionaryTree):
    """Cut the words in the dictionaryTree(stored in a BST) down to only entries with the same double letter"""
    splitWord = str.split(word)
    letterList = []
    double = ""
    # Check if the word has a double letter
    for letter in splitWord:
        if letter in letterList:
            double == letter
        else:
            letterList.append(letter)
    
    # If word does contain a double letter, then cut the dictionaryTree to only words with that double letter.
    if double != "":
        for words in dictionaryTree.items_pre_order:
            letter_count = 0
            # If the double letter is present in the word
            if double in word:
                # Search the word for two or more instances of letter. If there is, append word to dictionaryTree
                for letter in str.split(word):
                    if letter == double:
                        letter_count += 1
            # Checks if the double letter is really present twice or more
            if letter_count >= 2:
                dictionaryTree.insert(word)
        return dictionaryTree     

def wordLength(word, dictionaryTree):
    """Cut the number of words in the dictionaryTree to only ones with the same length as the scrambled word"""
    for entry in dictionaryTree:
        if len(entry) == len(word):
            dictionaryTree.insert(word)
    return dictionaryTree

def descramble(word, tree):
    """Takes the scrambled word and finds matches within the dictionaryTree """
    match = []
    
    # Helper functions
    dictionaryTree = firstLetter(scrambled_word, tree)
    doubleLetter(scrambled_word, dictionaryTree)
    wordLength(scrambled_word, dictionaryTree)
        
    # Creates a tree out of the pruned dictionaryTree
    tree = BinarySearchTree(dictionaryTree)
    
    for words in dictionaryTree:
        wordLetters = str.split(word)
        count = 0
        for letters in wordLetters:
            if letters == word[count]:
                count += 1
                if count == len(word):
                    match.append(word)
    return match

if __name__ == "__main__":
    # Word we want to unscramble
    scrambled_word = "toims"
    
    # Finds possible matches to the scrambled word
    matchList = descramble(scrambled_word, tree)
    print("Scramble: {} \n Matches: {}".format(scrambled_word, matchList))