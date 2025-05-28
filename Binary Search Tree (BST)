class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

# Example usage
if __name__ == "__main__":
    bst = BST()
    keys = [50, 30, 20, 40, 70, 60, 80]

    for key in keys:
        bst.root = bst.insert(bst.root, key)

    print("Inorder traversal of BST:")
    bst.inorder(bst.root)  # Output should be sorted

    print("\nSearch for 40:", "Found" if bst.search(bst.root, 40) else "Not found")
    print("Search for 100:", "Found" if bst.search(bst.root, 100) else "Not found")
