class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        def buildTrie(dictionary):
            root = TrieNode()
            for word in dictionary:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_word = True
            return root

        n = len(s)
        root = buildTrie(dictionary)
        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    dp[start] = min(dp[start], dp[end + 1])
        return dp[0]
        