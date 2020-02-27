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
            
            
            
            
            
if __name__ == '__main__':
    unittest.main()
        
        
        
    