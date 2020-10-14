# https://leetcode.com/problems/set-matrix-zeroes/

# The challenge is to set it in place
# So we cannot just make a new array and go from there
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            for c in range(C):
                # If it was originally 0, turn it into 0.2
                if matrix[r][c] == 0 or matrix[r][c] == 0.2:
                    for i in range(R):
                        if matrix[i][c] == 0 or matrix[i][c] == 0.2:
                            matrix[i][c] = 0.2
                        else:
                            # If we are changing it to 0, change it to 0.1
                            matrix[i][c] = 0.1
                    for j in range(C):
                        if matrix[r][j] == 0 or matrix[r][j] == 0.2:
                            matrix[r][j] = 0.2
                        else:
                            matrix[r][j] = 0.1
        
        for r in range(R):
            for c in range(C):
                # Change all elements which were originally 0 or meant to become 0
                if matrix[r][c] == 0.1 or matrix[r][c] == 0.2:
                    matrix[r][c] = 0
                    
# Time Complexity: O(N^3), because we go through each cell once and for each cell we go through its row and column
# Space Complexity: O(1), as we only create variables for the length
