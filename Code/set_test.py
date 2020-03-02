from set import TreeSet
import unittest

class TreeTest(unittest.TestCase):
    def test_init(self):
        elements = ['X', 'y', 'Z']
        set = TreeSet(elements)
        assert set.size is 3
        
    def test_size(self):
        elements = ['A', 'B', 'C', 'D', 'E']
        set = TreeSet(elements)
        assert set.size is 5
        
    def test_contains(self):
        elements = ['P', 'C', 'X', '1']
        set = TreeSet(elements)
        assert set.contains('P') is True
        assert set.contains('C') is True
        assert set.contains('1') is True
        assert set.contains('D') is False
        assert set.contains('J') is False
    
    def test_add(self):
        elements = ['L', 'M']
        set = TreeSet(elements)
        set.add('A')
        set.add('O')
        # Testing if it already exists within
        with self.assertRaises(KeyError):
            set.add('L') # Already exists
        with self.assertRaises(KeyError):
            set.add('O') # Already exists
            
        assert set.size is 4
        assert set.contains('L') is True
        
        assert set.contains('S') is False
            
    def test_remove(self):
        elements = ['I', 'D', 'W', 'T']
        set = TreeSet(elements)
        
        with self.assertRaises(KeyError):
            set.remove('K') # Doesn't exist
        with self.assertRaises(KeyError):
            set.remove('M') # Doesn't exist
        set.remove('I')
        set.remove('T')
        assert set.contains('U') is False
        assert set.contains('Q') is False
        with self.assertRaises(KeyError):
            set.remove('Q') # Doesn't exist anymore
            
    def test_union(self):
        elements = ['A', 'C', 'D', 'F']
        elements2 = ['A', 'B', 'D', 'F', 'G', 'H']
        elements3 = ['C', 'Y', 'T', 'A']
        set = TreeSet(elements)
        set2 = TreeSet(elements2)
        set3 = TreeSet(elements3)
        self.assertCountEqual(set.union(set2).tree.items_in_order(), ['A', 'B', 'C', 'D', 'F', 'G', 'H'])  # Ignore item order
        self.assertCountEqual(set.union(set3).tree.items_in_order(), ['A', 'C', 'D', 'F', 'T', 'Y'])  # Ignore item order

    def test_intersection(self):
        elements = ['0', 'B', 'C', 'K']
        elements2 = ['0', 'D', 'E', 'C', 'Y', 'K']
        elements3 = ['B', 'D', 'P', 'K', 'G', '9']
        set = TreeSet(elements)
        set2 = TreeSet(elements2)
        set3 = TreeSet(elements3)
        self.assertCountEqual(set.intersection(set2).tree.items_in_order(), ['0', 'C', 'K'])  # Ignore item order
        self.assertCountEqual(set.intersection(set3).tree.items_in_order(), ['B', 'K']) # Ignore item order

    def test_difference(self):
        elements = ['4', '7', '8', '9', '0']
        elements2 = ['4', '5', '6', '10', '8', '9']
        elements3 = ['1', '3', '5', '7', '0']
        set = TreeSet(elements)
        set2 = TreeSet(elements2)
        set3 = TreeSet(elements3)
        self.assertCountEqual(set.difference(set2).tree.items_in_order(), ['7', '0']) 
        self.assertCountEqual(set.difference(set3).tree.items_in_order(), ['4', '8', '9'])

    def test_is_subset(self):
        elements = ['Y', 'C', 'D']
        elements2 = ['C', 'G', 'U', 'D', 'T', 'Y']
        elements3 = ['P', 'H', 'Y', 'D', 'E', 'F']
        set1 = TreeSet(elements)
        set2 = TreeSet(elements2)
        set3 = TreeSet(elements3)
        assert set1.is_subset(set2) is False
        assert set1.is_subset(set3) is False
        assert set2.is_subset(set3) is False

if __name__ == '__main__':
    unittest.main()          
            
        
        
    