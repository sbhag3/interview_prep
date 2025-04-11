class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s, i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(index, s, path, ans):
            if index == len(s):
                ans.append(path[:])
                return

            for j in range(index, len(s)):
                if isPalindrome(s, index, j):
                    path.append(s[index:j+1])
                    backtrack(j + 1, s, path, ans)
                    path.pop()

        ans = []
        backtrack(0, s, [], ans)
        return ans
        