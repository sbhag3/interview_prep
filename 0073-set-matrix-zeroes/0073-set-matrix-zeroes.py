class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        change_row = []
        change_col = []

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    change_row.append(i)
                    change_col.append(j)

        for i in range(m):
            for j in range(n):
                if i in change_row or j in change_col:
                    matrix[i][j] = 0
        