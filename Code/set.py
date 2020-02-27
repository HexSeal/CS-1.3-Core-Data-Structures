from binarytree import BinaryTreeNode, BinarySearchTree

class TreeSet(object):
    """Initialize a new empty set structure, and add each element if a sequence is given"""
    def __init__(self, elements=None):
        self.tree = BinarySearchTree()
        self.size = 0
        self.element = BinaryTreeNode
        
        if elements is not None:
            for element in elements:
                self.add(element)
        
    def size(self):
        """Property that tracks the number of elements in constant time"""
        return self.size
        
    def contains(self, element):
        """return a boolean indicating whether element is in this set"""
        return self.tree.contains(element)
    
    def add(self, element):
        """add element to this set, if not present already"""
        if self.tree.contains(element):
            raise KeyError(f'{element} is already in tree.')
        else:
            self.tree.insert(element)
            self.size += 1
    
    def remove(self, element): 
        """remove element from this set, if present, or else raise KeyError"""
        if self.tree.contains(element) != True:
            raise KeyError(f'No such element exists: {element}')
        else:
            self.tree.delete(element)
            self.size -= 1
    
    def union(self, other_set): 
        """return a new set that is the union of this set and other_set"""
        for element in other_set:
            self.add(element)
    
    def intersection(self, other_set): 
        """return a new set that is the intersection of this set and other_set"""
        new_set = TreeSet()
        for element in self.tree.items_in_order():
            if other_set.contains(element):
                new_set.add(element) 
    
    def difference(self, other_set): 
        """return a new set that is the difference of this set and other_set"""
        new_set = TreeSet()
        for element in self.tree.items_in_order():
            if other_set.contains(element):
                other_set.remove(element)
                new_set.remove(element)
        return new_set
    
    def is_subset(self, other_set): 
        """return a boolean indicating whether other_set is a subset of this set"""
        currentElement = 0
        for element in other_set.hash.values():
            if self.contains(element):
                currentElement += 1
        return self.size == currentElement