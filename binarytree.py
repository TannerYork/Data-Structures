from queue import Queue


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
        return True if self.right is None and self.left is None else False

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return True if self.right is not None or self.left is not None else False

    def height(self, left_count=None, right_count=None):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)."""
        if left_count is None and right_count is None:
            left_count, right_count = 0, 0
        if self.is_leaf():
            return right_count if right_count > left_count else left_count
        if self.left is not None:
            left_count += self.left.height()
            left_count += 1
        if self.right is not None:
            right_count += self.right.height()
            right_count += 1
        return right_count if right_count > left_count else left_count


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
        downward path from this tree's root node to a descendant leaf node)."""
        return self.root.height() if self.root is not None else 0

    def contains(self, item):
        """Return True if this binary search tree contains the given item."""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found."""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree."""
        node = BinaryTreeNode(item)
        if self.is_empty():
            self.root = node
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        # Determin which side of the parent the new node should be added
        if parent is None:
            if item < self.root.data:
                self.root.left = node
            if item > self.root.data:
                self.root.right = node
        else:
            if item < parent.data:
                node.left = parent.left
                parent.left = node
            if item > parent.data:
                node.right = parent.right
                parent.right = node
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node."""
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # if the given item matches the node's data, return node
            if node.data == item:
                return node
            # if the given item is less than the node's data, decend left
            elif item < node.data:
                node = node.left
            # if the given item is greater than the node's data, decend right
            elif item > node.data:
                node = node.right
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion)."""
        # if starting node doesn't exist, return None
        if node is None:
            return None
        # if the given item matches the node's data, return node
        elif node.data is item:
            return node
        # if the given item is less than the node's data, recursively decend to node's left
        elif item < node.data:
            return self._find_node_recursive(item, node.left)
        # if the given item is greater than the node's data, recursively decend to node's right
        elif item > node.data:
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node."""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # if the given item matches the node's data, return the node's parent
            if node.data == item:
                return parent
            # if node should be the item's parent, return node
            if parent is not None:
                if item > node.data:
                    return node
                if item < node.data:
                    return node
            # if the given item is less than the node's data, decend left
            elif item < node.data:
                parent = node
                node = node.left
            # if the given item is greater than the node's data, decend right
            elif item > node.data:
                parent = node
                node = node.right
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""

        # if starting node doesn't exist, return None
        if node is None:
            return None
        # if the given item matches the node's data, return the parent
        if node.data is item:
            return parent
        # if node should be the item's parent, return node
        if parent is not None:
            if item > node.data:
                return node
            if item < node.data:
                return node
        # if the given item is less than the node's data, recursively decend left
        if item < node.data:
            return self._find_parent_node_recursive(item, node.left, node)
        # if the given item is greater than the node's data, recursively decend right
        if item > node.data:
            return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError."""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
            # self._traverse_in_order_iterative(self.root, items.append)
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        if node:
            # Traverse left subtree, if it exists
            self._traverse_in_order_recursive(node.left, visit)
            #  Visit this node's data with given function
            visit(node.data)
            # Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        # This can definetly be improved but this is what I've come up with so far
        stack = []
        visited = {}
        while node is not None:
            left, right = node.left, node.right
            if left is not None and right is not None:
                if node.data not in visited:
                    stack.append(node)
            if left is not None and left.data not in visited:
                node = left
                continue
            if node.data not in visited:
                visit(node.data)
                visited[node.data] = True
            if right is not None and right.data not in visited:
                stack.append(right)
                node = right
                continue
            node = stack[len(stack)-1] if len(stack) > 0 else None
            stack.pop() if len(stack) > 0 else stack

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
            # self._traverse_pre_order_iterative(self.root, items.append)
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        if node:
            visit(node.data)
            if node.left is not None:
                self._traverse_pre_order_recursive(node.left, visit)
            if node.right is not None:
                self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        stack = []
        while node is not None:
            visit(node.data)
            if node.left is not None:
                if node.right is not None:
                    stack.append(node.right)
                node = node.left
                continue
            elif node.right is not None:
                node = node.right
                continue
            node = stack[len(stack)-1] if len(stack) > 0 else None
            stack.pop() if len(stack) > 0 else stack

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
            # self._traverse_post_order_iterative(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        if node:
            self._traverse_post_order_recursive(node.left, visit)
            self._traverse_post_order_recursive(node.right, visit)
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        # This can definetly be improved but this is what I've come up with so far
        stack = []
        visited = {}
        while node is not None:
            right, left = node.right, node.left
            if left is not None and left.data not in visited:
                stack.append(node)
                if right is not None:
                    stack.append(right)
                node = left
                continue
            if right is not None and right.data not in visited:
                node = right
                continue
            visit(node.data)
            visited[node.data] = True
            node = stack[len(stack)-1] if len(stack) > 0 else None
            stack.pop() if len(stack) > 0 else stack

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
        Start at the given node and visit each node with the given function."""
        # Create a queue to store nodes not yet traversed in level-order
        queue = Queue()
        # Enqueue the given starting node
        queue.enqueue(start_node)
        while queue.is_empty() is False:
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
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