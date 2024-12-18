class Node:
    """
    A class representing a single node in a Binary Search Tree (BST).
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    A class representing a Binary Search Tree (BST) and its operations.
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    def search(self, key):
        """Search for a key in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current, key):
        if current is None:
            return current

        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            temp = self._min_value_node(current.right)
            current.key = temp.key
            current.right = self._delete_recursive(current.right, temp.key)

        return current

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """Perform in-order traversal of the BST."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current, result):
        if current is not None:
            self._inorder_recursive(current.left, result)
            result.append(current.key)
            self._inorder_recursive(current.right, result)


def test_binary_search():
    bst = BinarySearchTree()
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)

    print("In-order traversal after inserts:", bst.inorder_traversal())

    search_key = 40
    print(f"Search for {search_key}:", "Found" if bst.search(search_key) else "Not Found")

    delete_key = 30
    bst.delete(delete_key)
    print(f"In-order traversal after deleting {delete_key}:", bst.inorder_traversal())


if __name__ == "__main__":
    test_binary_search()
