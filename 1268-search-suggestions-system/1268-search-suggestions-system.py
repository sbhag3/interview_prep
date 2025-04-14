class TrieNode:
    def __init__(self):
        self.suggestions = []
        self.children = defaultdict(TrieNode)


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        root = TrieNode()
        for product in products:
            trav = root
            for char in product:
                if char not in trav.children:
                    trav.children[char] = TrieNode()
                trav = trav.children[char]
                if len(trav.suggestions) < 3:
                    trav.suggestions.append(product)

        ans = []
        trav = root
        for char in searchWord:
            if trav and char in trav.children:
                trav = trav.children[char]
                ans.append(trav.suggestions)
            else:
                trav = None
                ans.append([])
        return ans
        