from binarytree import BinaryTreeNode, BinarySearchTree

class TreeSet(object):
    """Initialize a new empty set structure, and add each element if a sequence is given"""
    def __init__(self, elements=None):
        self.tree = BinarySearchTree()
        self.element = BinaryTreeNode
        if elements is not None:
            for element in elements:
                self.add(element)
    
    @property    
    def size(self):
        """Property that tracks the number of elements in constant time"""
        return self.tree.size
        
    def contains(self, element):
        """return a boolean indicating whether element is in this set
        Running time: O(log n) since we just search through a binary tree"""
        return self.tree.contains(element)
    
    def add(self, element):
        """add element to this set, if not present already
        Running time: O(log n) because we must binary search"""
        if self.tree.contains(element):
            raise KeyError(f'{element} is already in tree.')
        else:
            self.tree.insert(element)
    
    def remove(self, element): 
        """remove element from this set, if present, or else raise KeyError
        Running time: 
        Best Case: O(h) because we have to either scale the tree or move everything down
        once found.
        Worst Case: O(n) because the element could be the last we check in the tree."""
        if self.tree.contains(element) != True:
            raise KeyError(f'No such element exists: {element}')
        else:
            self.tree.delete(element)
    
    def union(self, other_set): 
        """return a new set that is the union of this set and other_set
        Best and worst case: (m + n) * log m because we add the length of each set to the time of the .add calls"""
        # m log m + n*2logm = (m + 2n) * log m =
        # (m + n) * log m
        new_set = TreeSet()
        for element in self.tree.items_pre_order(): # O(h(self))
            new_set.add(element) # + O(m)
        
        # Adds remaining other_set elements
        for element in other_set.tree.items_pre_order():
            if not new_set.contains(element): # O(log m)
                new_set.add(element) # +O(log m)
            
        return new_set
    
    def intersection(self, other_set): 
        """return a new set that is the intersection of this set and other_set
        Best case/worst case: O(log n) due to binary search"""
        new_set = TreeSet()
        for element in self.tree.items_in_order():
            if other_set.contains(element):
                new_set.add(element)
        return new_set
    
    def difference(self, other_set): 
        """return a new set that is the difference of this set and other_set
        Best/Worst case: O(n) because we require checking all nodes"""
        new_set = TreeSet()
        for element in self.tree.items_in_order():
            new_set.add(element)

        for element in other_set.tree.items_in_order():
            if new_set.contains(element):
                new_set.remove(element)
        return new_set

    def is_subset(self, other_set): 
        """return a boolean indicating whether other_set is a subset of this set
        Best case:e O(1), incase the size is bigger than other_set and we don't need to do anything.
        Worst case: O(n), if we must traverse through all nodes"""
        if self.size > other_set.size:
            return False
        
        for element in other_set.tree.items_in_order():
            if not self.contains(element):
                return False
                
        return True