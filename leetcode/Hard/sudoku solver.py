# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def checkValid(self, board, x, y, val):
        # Check rows
        for i in range(9):
            if board[i][y] == str(val):
                return False
        # Check columns
        for j in range(9):
            if board[x][j] == str(val):
                return False
        # Check box
        bx = x - (x % 3)
        by = y - (y % 3)
        for i in range(bx, bx+3):
            for j in range(by, by+3):
                if board[i][j] == str(val):
                    return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        EMP = '.'
        def helper(x, y):
            # Get the next x, y such that board[x][y] is empty
            # If we can't, return True
            found = False
            for i in range(9):
                for j in range(9):
                    if not found:
                        if board[i][j] == EMP:
                            x = i
                            y = j
                            found = True
            if not found:
                return True
            
            for val in range(1, 10):
                if self.checkValid(board, x, y, val):
                    board[x][y] = str(val)
                    if helper(x, y+1):
                        return True
                    board[x][y] = EMP
        
        helper(0, 0)
