class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf
        self.next = None  

class BPlusTree:
    def __init__(self, order=3):
        self.root = BPlusTreeNode(is_leaf=True)
        self.order = order

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.order - 1:
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            idx = self._find_index(node.keys, key)
            child = node.children[idx]
            if len(child.keys) == self.order - 1:
                self._split_child(node, idx)
                if key > node.keys[idx]:
                    idx += 1
            self._insert_non_full(node.children[idx], key)

    def _split_child(self, parent, index):
        node = parent.children[index]
        mid = self.order // 2

        if node.is_leaf:
            right = BPlusTreeNode(is_leaf=True)
            right.keys = node.keys[mid:]
            node.keys = node.keys[:mid]


            right.next = node.next
            node.next = right

            parent.keys.insert(index, right.keys[0])
            parent.children.insert(index + 1, right)
        else:
            right = BPlusTreeNode()
            right.keys = node.keys[mid+1:]
            right.children = node.children[mid+1:]
            split_key = node.keys[mid]

            node.keys = node.keys[:mid]
            node.children = node.children[:mid+1]

            parent.keys.insert(index, split_key)
            parent.children.insert(index + 1, right)

    def _find_index(self, keys, key):
        for i, item in enumerate(keys):
            if key < item:
                return i
        return len(keys)

    def print_tree(self):
        queue = [self.root]
        level = 0
        while queue:
            print("Level", level, ": ", end="")
            next_queue = []
            for node in queue:
                print(node.keys, end=" ")
                if not node.is_leaf:
                    next_queue.extend(node.children)
            print()
            queue = next_queue
            level += 1

    def print_leaves(self):
        node = self.root
        while not node.is_leaf:
            node = node.children[0]
        print("Leaves: ", end="")
        while node:
            print(node.keys, end=" -> ")
            node = node.next
        print("None")
