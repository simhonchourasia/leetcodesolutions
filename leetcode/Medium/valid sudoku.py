# https://leetcode.com/problems/valid-sudoku/submissions/

class Solution:
    def checkBox(self, board, x, y):
        nums = []
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] != ".":
                    if board[i][j] in nums:
                        return False
                    nums.append(board[i][j])
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check boxes
        starters = [0, 3, 6]
        for i in starters:
            for j in starters:
                if not self.checkBox(board, i, j):
                    return False
        
        # Check rows
        for i in range(9):
            nums = []
            for j in range(9):
                tmp = board[i][j]
                if tmp != ".":
                    if tmp in nums:
                        return False
                    nums.append(tmp)
        
        # Check columns
        for j in range(9):
            nums = []
            for i in range(9):
                tmp = board[i][j]
                if tmp != ".":
                    if tmp in nums:
                        return False
                    nums.append(tmp)
        return True
