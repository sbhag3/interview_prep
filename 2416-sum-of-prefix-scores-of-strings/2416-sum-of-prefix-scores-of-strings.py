class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        trav = self.root
        for c in word:
            if c not in trav.children:
                trav.children[c] = TrieNode()
            trav.children[c].count += 1
            trav = trav.children[c]

    def count(self, s):
        trav = self.root
        ans = 0
        for c in s:
            ans += trav.children[c].count
            trav = trav.children[c]
        return ans

    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        for i in range(n):
            self.insert(words[i])
        scores = [0] * n
        for i in range(n):
            scores[i] = self.count(words[i])
        return scores
        