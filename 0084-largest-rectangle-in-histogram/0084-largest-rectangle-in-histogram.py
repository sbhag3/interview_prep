class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st = [-1] # end of list
        ans = 0
        for i in range(len(heights)):
            while st[-1] != -1 and heights[st[-1]] >= heights[i]:
                curr_height = heights[st.pop()]
                curr_width = i - st[-1] - 1
                ans = max(ans, curr_height * curr_width)
            st.append(i)
            
        while st[-1] != -1:
            curr_height = heights[st.pop()]
            curr_width = len(heights) - st[-1] - 1
            ans = max(ans, curr_height * curr_width)
        return ans


        
        
        