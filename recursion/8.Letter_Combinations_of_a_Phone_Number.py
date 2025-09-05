from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        def helper(idx, curr_str):
            if idx == len(digits):
                result.append(curr_str)
                return
            for ch in digit_map[digits[idx]]:
                helper(idx+1, curr_str + ch)
        helper(0, "")
        return result 