class Node():
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        return self.head

    def __next__(self):
        data = self.iter_node.data
        self.iter_node = self.iter_node.next
        return data

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length +=1
        else:
            self.tail.next = node
            node.prev = self.tail
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
           raise ValueError(f'Item not found: {item}')

        node = self.head
        while node is not None and node.data is not item:
            node = node.next

        if node is self.tail and node.data is not item:
            raise ValueError(f'Item not found: {item}')

        if node is self.head:
            self.head = node.next
            if node is self.tail:
                self.head = None
                self.tail = None
        elif node is self.tail:
            self.tail = node.prev
        else:
            prev_node.next = node.next


def main():
    dll = DoublyLinkedList()
    # Test append
    dll.append(1)
    assert dll.head.data is 1
    assert dll.tail.data is 1
    dll.append(2)
    assert dll.tail.data is 2
    dll.append(3)
    assert dll.tail.data is 3
    assert dll.length is 3
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