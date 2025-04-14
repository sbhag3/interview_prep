class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def backtrack(nums, index, path, ans):
            if index == len(nums):
                ans.append(path[:])
                return

            path.append(nums[index])
            backtrack(nums, index + 1, path, ans)
            path.pop()
            backtrack(nums, index + 1, path, ans)

        ans = []
        backtrack(nums, 0, [], ans)

        res = 0
        for subset in ans:
            total = 0
            for num in subset:
                total ^= num
            res += total
        return res        