class TreeNode:
    def __init__(self):
        # Dictionary approach (more flexible for any character set)
        self.children = {}
        self.isWord = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TreeNode()
            curr_node = curr_node.children[char]
        curr_node.isWord = True


    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        return curr_node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True
        