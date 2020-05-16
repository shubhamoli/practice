"""
    Leetcode #211
"""


from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = TrieNode()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self._root
        for w in word:
            # each child will become TrieNode object
            # see, defaultdict implementation above
            node = node.children[w]

        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self._root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word) -> bool:
        if not word:
            if node.isWord:
                self.res = True
            return

        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])

        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])



if __name__ == "__main__":

    wordDict = WordDictionary()

    wordDict.addWord("bad")
    wordDict.addWord("dad")
    wordDict.addWord("mad")

    assert wordDict.search("pad") == False
    assert wordDict.search("bad") == True
    assert wordDict.search(".ad") == True
    assert wordDict.search("b..") == True

