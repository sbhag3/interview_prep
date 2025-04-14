class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(curr, num):
            if len(curr) == k:
                ans.append(curr[:])
                return

            need = k - len(curr)
            remain = n - num + 1
            avail = remain - need
            
            for num in range(num, num + avail + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()

        ans = []
        backtrack([], 1)
        return ans
        