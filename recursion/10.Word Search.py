from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def find(i, j, idx):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = '$'
            for dx, dy in directions:
                if find(i + dx, j + dy, idx + 1):
                    board[i][j] = temp 
                    return True
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i, j, 0):
                    return True

        return False