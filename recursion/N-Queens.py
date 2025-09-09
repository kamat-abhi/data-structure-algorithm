from typing import List

#Approach 1: Backtracking
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = ["." * n for _ in range(n)]

        def isValid(board, row, col):
            #upward check
            i = row-1
            while i>=0:
                if board[i][col] == "Q":
                    return False
                i -= 1
            #left diagonal upward check
            i, j = row - 1, col - 1
            while i>=0 and j>=0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            #right diagonal upward check
            i, j = row - 1, col + 1
            while i>=0 and j<n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        def solve(board, row):
            if row == n:
                result.append(board[:])
                return
            for col in range(n):
                if isValid(board, row, col):
                    row_list = list(board[row])
                    row_list[col] = "Q"
                    board[row] = "".join(row_list)
                    solve(board, row+1)
                    row_list[col] = "."
                    board[row] = "".join(row_list)

        solve(board, 0)
        return result                    