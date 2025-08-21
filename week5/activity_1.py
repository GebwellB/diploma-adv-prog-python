# 3) BST (Binary Search Tree) Search
# [Slide: Binary Search Tree]
# left subtree keys < node.key < right subtree keys.
# Search is O(log n) if balanced; worst case O(n) if skewed.
class BSTNode:
    # __slots__ tells Python to only allow these three attributes.
    __slots__ = ("key", "left", "right")
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# insert a key into the BST
def insert(root = None, key = 0):
    # if the tree is empty, create a new node as root
    if root is None:
        return BSTNode(key)
    # if smaller, insert into the left subtree
    if key < root.key:
        root.left = insert(root.left, key)

    # if larger, insert into the right subtree
    if key > root.key:
        root.right = insert(root.right, key)

    # return the root, hint: this may be unchanged
    return root

# Search for a key in the BST
def bst_search_iterative(key, target):
    """Return the node with key == key, or None if not found (recursive).

    Args:
        key (int): It's a key
        target (int): It's a target
    """
    # Base case: empty tree or we’ve reached a leaf

    # start at the root
    current = key

    # traverse the tree until None is given
    while current is not None:
        # if the key matches, return the node
        print(type(current))
        if current.key == target:
            return current

        # if the key is smaller, go left; otherwise, go right
        elif target < current.key:
            current = current.left
        else:
            current = current.right
    # if not found, return None
    return None

def bst_search_recursive(root, key):
    """Return the node with key == key, or None if not found (recursive)."""
    # Base case: empty tree or we’ve reached a leaf
    if root is None:
        return None

    # if key matches, return this node
    if root.key == key:
        return root

    # if key is smaller, search in left subtree
    elif key < root.key:
        return bst_search_recursive(root.left, key)

    # if key is larger, search in right subtree
    else:
        return bst_search_recursive(root.right, key)

if __name__ == '__main__':

    root = None
    for key in [50, 30, 70, 20, 40, 60, 80, 100, 20, 35, 40,
        25, 45, 65, 75, 90, 10, 5, 85, 95, 15, 33, 37, 43, 47,
        55, 58, 62, 67, 72, 78, 82, 88, 92, 97, 99, 105, 110, 115,
        22, 28, 32, 36, 38, 42, 44, 46, 48, 52, 53, 56, 59, 61,
        63, 66, 68, 69, 73, 76, 77, 79, 81, 83, 84, 86, 87, 89,
        91, 93, 94, 96, 98, 101, 102, 103, 104, 106, 107, 108,
        109, 111, 112, 113, 114, 116, 117, 118, 119, 120,
        27, 29, 31, 34, 39, 41, 49, 51, 54, 891]:
        root = insert(root, key)

    # Test iterative search
    found = bst_search_iterative(root, 60)
    print("Iterative search for 60:", found.key if found else "Not found")

    # Test recursive search
    found = bst_search_recursive(root, 25)
    print("Recursive search for 25:", found.key if found else "Not found")