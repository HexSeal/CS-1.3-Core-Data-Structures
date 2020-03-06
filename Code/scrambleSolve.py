from itertools import permutations
import strings
import os

dictionary= {}
def makeDictionary(length):
    with open("/usr/share/dict/words", 'r') as f:
        for word in f:
            #Remove endline characters
            word = word.strip().lower()
            
            #Also only sets the word if it equals the length of the scrambled words
            if len(word) == length:
                dictionary[word] = 1
        return dictionary

def scrambleSolve(scrambledWord):
    scrambledWord = "iomst"
    splitword = str.split("", )
    perm = permutations(splitword)
    matches = []
    
    for word in perm:
        for entry in dictionary:
            if entry == word:
                matches.append(entry)
    return matches

if __name__ == "__main__":
    scrambledWord = "oimst"
    length = len(scrambledWord)
    dictionary = makeDictionary(length)
    matched = scrambleSolve(scrambledWord)
    print(matched)