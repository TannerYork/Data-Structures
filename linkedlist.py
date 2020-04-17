class Node():
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.iter_node = None

    def __iter__(self):
        self.iter_node = self.head
        return self

    def __next__(self):
        data = self.iter_node.data
        self.iter_node = self.iter_node.next
        return data
        
    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

    def contains(self, item):
        node = self.head
        while node is not None:
            if node.data is item:
                return True
            node = node.next
        return False

    def delete(self, item):
        if self.head is None:
            raise ValueError(f'Could not find item: {item}')

        prev_node = None
        node = self.head
        next_node = self.head.next
        while node is not None and node.data is not item:
            prev_node = node
            node = next_node
            next_node = node.next
        
        if node is self.tail and node.data is not item:
            raise ValueError(f'Could not find item: {item}')

        if node is self.head:
            self.head = next_node
            self.length -= 1
            if node is self.tail:
                self.head = None
                self.tail = None
        elif node is self.tail:
            self.tail = prev_node
            self.length -= 1
        else:
            prev_node.next = next_node
            self.length -= 1

def main():
    dll = LinkedList()
    # Test append
    dll.append(1)
    assert dll.head.data is 1
    assert dll.tail.data is 1
    dll.append(2)
    assert dll.tail.data is 2
    dll.append(3)
    assert dll.tail.data is 3
    assert dll.length is 3
    # Test iteration
    for node in dll:
        print(node)
    # Test containes
    assert dll.contains(3)
    # Test delete
    dll.delete(3)
    assert dll.tail.data is 2
    dll.delete(2)
    assert dll.tail.data is 1
    dll.delete(1)
    assert dll.tail is None
    assert dll.head is None
    print('passed tests')

if __name__ == '__main__':
    main()