class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf
        self.next = None  # Used for leaf node linking

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
        split_key = node.keys[mid]

        right = BPlusTreeNode(is_leaf=node.i_
