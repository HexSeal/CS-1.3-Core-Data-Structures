#!python

from linkedlist import LinkedList, Node


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} iteront={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.length() == 0

    def length(self):
        """Return the number of items in this queue."""
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) because we have instant access to the tail of the queue"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if not self.is_empty():
            return self.list.head.data
        return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) because we have instant access to the head of the queue"""
        if self.is_empty():
            raise ValueError("Queue is Empty")

        front = self.list.head.data
        self.list.delete(front)

        return front
    
# Helped by @github.com/jon-infante
    def push_front(self, item):
        """Insert item to the front of the queue.
        Running time: O(1) - We have instant access to the head."""
        self.list.append(item)

    def push_back(self, item):
        """Insert item to the back of the queue.
        Running time: O(1) - We have instant access to the tail."""
        self.list.prepend(item)

    def pop_front(self):
        """Delete item at the front of the queue. Raise ValueError if the
        queue is empty.
        Running time: O(1) - We have instant access to the head.
        """
        if self.is_empty():
            raise ValueError("Queue is Empty")

        front = self.list.head.data
        self.list.delete(front)

        return front

    def pop_back(self):
        """Delete item at the back of the queue. Raise ValueError if the
        queue is empty.
        Running time: O(n) - We have to traverse the length of the linked list.
        """
        if self.is_empty():
            raise ValueError("Queue is Empty")

        back = self.list.tail.data
        self.list.delete(back)

        return back


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if self.list == []:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) because we add it to the back of queue which doesn't require iteration"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if not self.is_empty():
            return self.list[0]
        return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) because we have instant access to index 0"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        
        front = self.list[0]
        self.list.pop(0)
        
        return front
        
# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
