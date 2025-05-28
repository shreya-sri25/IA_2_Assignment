RED = True
BLACK = False

class Node:
    def __init__(self, key):
        self.key = key
        self.color = RED  # New nodes are red by default
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NULL = Node(None)
        self.NULL.color = BLACK
        self.root = self.NULL

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NULL
        new_node.right = self.NULL
        parent = None
        curr = self.root

        while curr != self.NULL:
            parent = curr
            if new_node.key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = RED
        self.fix_insert(new_node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k != self.root and k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == RED:  # Case 1
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:  # Case 2
                        k = k.parent
                        self.left_rotate(k)
                    # Case 3
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == RED:
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
        self.root.color = BLACK

    def inorder(self, node):
        if node != self.NULL:
            self.inorder(node.left)
            print(f"{node.key}({ 'R' if node.color else 'B' })", end=' ')
            self.inorder(node.right)

    def display(self):
        print("Inorder traversal of Red-Black Tree:")
        self.inorder(self.root)
        print()
