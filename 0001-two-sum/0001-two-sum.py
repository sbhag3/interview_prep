class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}
        for i in range(len(nums)):
            cmpl = target - nums[i]
            if cmpl in mp:
                return [i, mp[cmpl]]
            mp[nums[i]] = i

        return []
        