class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            ans.append(list(path))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # skip duplicates
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        nums.sort()
        ans = []
        backtrack(0, [])
        return ans

        