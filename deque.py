from linkedlist import LinkedList

class LinkedDeque(object):
    def __init__(self, iterable=None):
        """Initialize this deque and enqueue items, if any."""
        self.list = LinkedList()   
        if iterable is not None:
            for item in iterable:
                self.push_back(item)
    
    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Deque({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return False if self.list.head else True

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size
    
    def push_front(self, item):
        """Prepend given item before the deque list's head"""
        self.list.prepend(item)

    def push_back(self, item):
        """Append given item to the end of the deque"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this deque without removing it,
        or None if this queue is empty."""
        return self.list.head.data if self.list.head else None

    def back(self):
        """Return the item at the back of this deque without removing it,
        or None if this queue is empty."""
        return self.list.tail.data if self.list.tail else None

    def pop_front(self):
        """Pop the first item in the deque or None"""
        if self.length() == 0:
            return None
        data = self.list.head.data
        self.list.delete(data)
        return data

    def pop_back(self):
        """Pop the last item in the deque or None"""
        if self.length() == 0:
            return None
        data = self.list.tail.data
        self.list.delete(data)
        return data


class ArrayDeque(object):
    def __init__(self, iterable=None):
        """Initialize this deque and enqueue items, if any."""
        self.list = list()   
        if iterable is not None:
            for item in iterable:
                self.push_back(item)
    
    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return True if len(self.list) == 0 else False

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)
    
    def front(self):
        """Return the item at the front of this deque without removing it,
        or None if this queue is empty."""
        return self.list[0] if len(self.list) > 0 else None

    def back(self):
        """Return the item at the front of this deque without removing it,
        or None if this queue is empty."""
        return self.list[len(self.list)-1] if len(self.list) > 0 else None

    def push_front(self, item):
        """Prepend given item before the deque list's head"""
        self.list.insert_at(0, item)

    def push_back(self, item):
        """Append given item to the end of the deque"""
        self.list.append(item)

    def pop_front(self):
        """Pop the first item in the deque or None"""
        if self.length() == 0:
            return None
        data = self.list[len(self.list)-1]
        self.list.remove(data)
        return data

    def pop_back(self):
        """Pop the last item in the deque or None"""
        if self.length() == 0:
            return None
        data = self.list[len(self.list)-1]
        self.list.remove(data)
        return data