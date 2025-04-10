class Solution(object):
    def helper(self, nums, i, ans):
            l, r = i + 1, len(nums) - 1
            while l < r:
                add = nums[i] + nums[l] + nums[r]
                if add < 0:
                    l += 1
                elif add > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.helper(nums, i, ans)
        return ans
        