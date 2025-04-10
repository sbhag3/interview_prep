class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [] # output
        q = deque() # indices queue
        left, right = 0, 0 # two pointer

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if right + 1 >= k:
                ans.append(nums[q[0]])
                left += 1
            right += 1

        return ans

        