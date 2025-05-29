class RadixNode:
    def __init__(self):
        self.children = {}  
        self.is_end = False

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def insert(self, word):
        node = self.root
        while word:
            for key in node.children:
                common_prefix_len = self._common_prefix_length(key, word)
                if common_prefix_len > 0:
                    if common_prefix_len < len(key):
                        # Split node
                        existing_child = node.children.pop(key)
                        node.children[key[:common_prefix_len]] = RadixNode()
                        node.children[key[:common_prefix_len]].children[key[common_prefix_len:]] = existing_child
                        node = node.children[key[:common_prefix_len]]
                    else:
                        node = node.children[key]
                    word = word[common_prefix_len:]
                    break
            else:
                node.children[word] = RadixNode()
                node.children[word].is_end = True
                return
        node.is_end = True

    def search(self, word):
        node = self.root
        while word:
            for key in node.children:
                if word.startswith(key):
                    word = word[len(key):]
                    node = node.children[key]
                    break
            else:
                return False
        return node.is_end

    def _common_prefix_length(self, s1, s2):
        i = 0
        while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
            i += 1
        return i
