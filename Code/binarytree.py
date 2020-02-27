#!python
from queue import LinkedQueue

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left == None and self.right == None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return (self.left != None) or (self.right != None)
    
    def count_edges(self, direction):
        """Count the height of a node. Takes in the direction parameter to recursively iterate through and determine if the left
        or right side will be used to determine the height of the tree"""
        if self.is_leaf():
            return 0
        elif direction == "left" or self.right is None:
            return 1 + self.left.count_edges('left')
        elif direction == "right" or self.left is None:
            return 1 + self.right.count_edges('right')

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best and worst case running time: O(h) where h is the height of the tree. The bigger the height, the more we have to iterate throug
        to get to the end"""
        left_height = 0
        right_height = 0
        # Check if left child has a value and if so calculate its height
        if self.left != None:
            left_height += self.count_edges('left')
        # Check if right child has a value and if so calculate its height
        if self.right != None:
            right_height += self.count_edges('right')
        # Return one more than the greater of the left height and right height
        if left_height > right_height:
            return left_height
        else:
            return right_height

class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best and worst case running time: O(h), we only have to traverse one path to get to the bottom and find the height"""
        if self.root.data != None:
            return self.root.height()
        return None

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: O(1), because the item could be the root of the tree.
        Worst case running time: O(n), the node could be a leaf"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(1) if we find it immediately
        Worst case running time: O(n) if we have to traverse through all the nodes to find the item"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        
        if node:
            return node.data
        return None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: O(1) if the tree is empty and we just have to create a new node?
        Worst case running time: O(log n) because at worst we have to traverse through nodes with binary search"""
        # Handle the case where the tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        
        # If the item is less than the parent node, go down the left side of the tree
        if item < parent.data:
            parent.left = BinaryTreeNode(item)
        
        # If the item is more than the parent node, then go down the right side of the tree
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)

        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(1) because the item could be the root node
        Worst case running time: O(log n) because at worst the item is the last """
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if node.data == item:
                # Return the found node
                return node
            
            elif item < node.data:
                node = node.left

            elif item > node.data:
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(1) because the item could be the root node
        Worst case running time: O(log n) because at worst the item is the last """
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Best case running time: O(1) because the item could be the root node
        Worst case running time: O(log n) because at worst the item is the last """
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data:
                # Return the parent of the found node
                return parent

            elif item < node.data:
                parent = node
                node = node.left

            elif item > node.data:
            # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)
        #  Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)

    def find_inorder_successor(self, node):
        items = self.items_in_order()
        for i in range(len(items)):
            if items[i] == node.data:
                return BinaryTreeNode(items[i+1])

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case running time: O(h) if we find the node on the first branch with no children
        Worst case running time: O(n) if we have to traverse everything to find the node, and more if the node had two children"""
        # Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        if self.contains(item) == False:
            raise ValueError()
        node = self._find_node_recursive(item, self.root)
        parent = self._find_parent_node_recursive(item, self.root)

        if node == self.root:
            if self.root.is_leaf():
                self.root = None
                return

            new_node = BinaryTreeNode(self.find_inorder_successor(node).data)
            self.delete(new_node.data)

            if node.left != None:
                new_node.left = node.left
            if node.right != None:
                new_node.right = node.right
            self.root = new_node

        # No children
        elif (node.left == None) and (node.right == None):
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        ### 1 child:
        # Left child
        elif(node.left != None) and (node.right == None):
            # another node on the left
            if node.data < parent.data:
                #node is on the left
                parent.left = node.left
            else:
                #node is on the right
                parent.right = node.left
        # Right child
        elif(node.left == None) and (node.right != None):
            # another node on the right
            if node.data < parent.data:
                #node is on the left
                parent.left = node.right
            else:
                #node is on the right
                parent.right = node.right
        # 2 children
        else:
            new_node = BinaryTreeNode(self.find_inorder_successor(node).data)
            self.delete(new_node.data)

            new_node.left = node.left
            new_node.right = node.right

            if node.data < parent.data:
                #node is on the left
                parent.left = new_node
            else:
                #node is on the right
                parent.right = new_node
            # node = None


    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n), where n is the number of entries. This is assuming the tree is optimized to be balanced.
        Memory usage: O(h), where h is the height of the tree. The time it takes to get from root to leaf depends on how tall the tree is."""
        # Traverse left subtree, if it exists
        if node is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
            visit(node.data)
        # Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n), where n is the number of entries. This is assuming the tree is optimized to be balanced.
        Memory usage: O(h), where h is the height of the tree. The time it takes to get from root to leaf depends on how tall the tree is."""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n), where n is the number of entries. This is assuming the tree is optimized to be balanced.
        Memory usage: O(h), where h is the height of the tree. The time it takes to get from root to leaf depends on how tall the tree is."""
        # Visit this node's data with given function
        if node is not None:
            visit(node.data)
        # Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        
        Running time: O(n), where n is the number of entries. This is assuming the tree is optimized to be balanced.
        Memory usage: O(h), where h is the height of the tree. The time it takes to get from root to leaf depends on how tall the tree is."""
        if node is None:
            return
        
        if node.left is not None:
        # Traverse left subtree, if it exists
            self._traverse_post_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)
        # Visit this node's data with given function
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n), for each node
        Memory usage: O(b) because we have to traverse the bredth/width of the tree on each layer before we can go on to the next"""
        # Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.list.length() == 0:
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left != None:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right != None:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
