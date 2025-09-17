"""
1. Find an empty cell: Scan the board (from left to right)
3. Try Digits: For each empty cell, try placing digits 1-9
4. check validity: For each number we try, check if it's valid in the current row, column, and 3*3 sub-box
5. Recursion: If placing the number is valid, place it and recursively attempt to solve the rest of the board
6. Backtrack: If placing the number doesn't lead to a solution, remove it (backtrack) and try the next number
7. If no number works, return False (trigger backtracking)
8. If the board is completely filled, return True (solved)
"""
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    box_index = (r // 3) * 3 + (c // 3)
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        box_index = (r // 3) * 3 + (c // 3)
                        for num_char in "123456789":
                            if (
                                num_char not in rows[r]
                                and num_char not in cols[c]
                                and num_char not in boxes[box_index]
                            ):

                                board[r][c] = num_char
                                rows[r].add(num_char)
                                cols[c].add(num_char)
                                boxes[box_index].add(num_char)

                                if solve():
                                    return True
                                board[r][c] = "."
                                rows[r].remove(num_char)
                                cols[c].remove(num_char)
                                boxes[box_index].remove(num_char)
                        return False
            return True

        solve()