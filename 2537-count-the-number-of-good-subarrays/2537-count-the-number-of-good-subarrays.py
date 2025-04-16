class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        same = 0
        right = -1
        count = Counter()
        ans = 0

        for left in range(n):
            while same < k and right + 1 < n:
                right += 1
                same += count[nums[right]]
                count[nums[right]] += 1
            if same >= k:
                ans += (n - right)

            count[nums[left]] -= 1
            same -= count[nums[left]]

        return ans
        