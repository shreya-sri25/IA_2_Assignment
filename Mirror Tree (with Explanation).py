class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to convert tree to its mirror
def mirror(root):
    if root is None:
        return None

    # Step 1: Mirror left and right subtrees
    mirror(root.left)
    mirror(root.right)

    # Step 2: Swap the left and right children
    root.left, root.right = root.right, root.left

    return root

# Function for inorder traversal (for checking)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Driver code
if __name__ == "__main__":
    # Construct this binary tree
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Inorder of original tree:")
    inorder(root)

    mirror(root)

    print("\nInorder of mirror tree:")
    inorder(root)
