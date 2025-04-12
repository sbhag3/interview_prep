class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [] 
        n = len(nums)

        def backtrack(nums, index, path, ans):
            if index == n: # we’ve made the total number of decisions that we can
                ans.append(path[:]) # append the current path state to the answer
                return
            path.append(nums[index]) # make the decision of using the element
            # recurse
            backtrack(nums, index + 1, path, ans)
            path.pop() # “backtrack” decision and find remaining paths
            backtrack(nums, index + 1, path, ans)

        backtrack(nums, 0, [], ans)
        return ans

        
        