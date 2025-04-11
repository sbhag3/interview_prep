class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(n, first, curr, nums, output):
            output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(n, i + 1, curr, nums, output)
                curr.pop()

        output = []
        n = len(nums)
        backtrack(n, 0, [], nums, output)
        return output
        