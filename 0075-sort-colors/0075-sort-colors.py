class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        curr = 0
        red = 0
        blue = len(nums) - 1

        while curr <= blue:
            if nums[curr] == 0:
                # red
                nums[red], nums[curr] = nums[curr], nums[red]
                red += 1
                curr += 1
            elif nums[curr] == 2:
                # blue
                nums[curr], nums[blue] = nums[blue], nums[curr]
                blue -= 1
            else:
                curr += 1
        