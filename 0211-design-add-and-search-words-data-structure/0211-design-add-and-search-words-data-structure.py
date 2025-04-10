class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        trav = self.root
        for char in word:
            if char not in trav.children:
                trav.children[char] = TrieNode()
            trav = trav.children[char]
        trav.is_end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(trav, i):
            if i == len(word):
                return trav.is_end_of_word
            char = word[i]
            if char == '.':
                return any(dfs(child, i + 1) for child in trav.children.values())
            if char not in trav.children:
                return False
            return dfs(trav.children[char], i + 1)
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)