class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True    

    def search(self, word: str) -> bool:

        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.word

            char = word[index]

            if char == ".":
                return any(dfs(child, index + 1) for child in node.children.values())

            if char not in node.children:
                return False

            return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)
