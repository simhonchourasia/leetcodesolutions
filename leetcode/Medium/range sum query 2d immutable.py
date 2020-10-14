# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix)>0 and len(matrix[0]):
            self.R = len(matrix)
            self.C = len(matrix[0])
            # Create 2D prefix-sum array
            self.psa = [[0 for c in range(self.C+1)] for r in range(self.R+1)]
            # Update values in prefix sum array, doing the edges first
            for c in range(1, self.C+1):
                self.psa[1][c] = self.psa[1][c-1]+matrix[0][c-1]
            for r in range(1, self.R+1):
                self.psa[r][1] = self.psa[r-1][1]+matrix[r-1][0]
            for r in range(1, self.R+1):
                for c in range(1, self.C+1):
                    self.psa[r][c] = self.psa[r-1][c]+self.psa[r][c-1]-self.psa[r-1][c-1]+matrix[r-1][c-1]
        else:
            return
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Formula to go from 2D prefix sum array to the sum of a rectangle in the original array
        return self.psa[row2+1][col2+1]-self.psa[row2+1][col1]-self.psa[row1][col2+1]+self.psa[row1][col1]

# Time Complexity: O(R*C), where R, C are the number of rows and columns
