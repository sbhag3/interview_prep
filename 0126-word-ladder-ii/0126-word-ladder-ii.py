class Solution(object):
    def findLadders(self, begin_word, end_word, word_list):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(word_list)
        if end_word not in word_set:
            return []

        # Step 1: BFS to build reverse graph (child -> set of parents)
        parents = defaultdict(set)
        level = {begin_word}
        word_len = len(begin_word)
        found = False

        while level and not found:
            next_level = defaultdict(set)
            for word in level:
                word_set.discard(word)
            for word in level:
                for i in range(word_len):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in word_set:
                            next_level[new_word].add(word)
                            if new_word == end_word:
                                found = True
            level = next_level
            for word in next_level:
                parents[word].update(next_level[word])

        # Step 2: DFS backtracking from end_word to begin_word
        res = []
        def dfs(word, path):
            if word == begin_word:
                res.append(path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [p])

        if found:
            dfs(end_word, [end_word])

        return res
        