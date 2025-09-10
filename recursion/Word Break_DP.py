from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        return self.solve(0, s, wordDict, memo)

    def solve(self, idx, s, wordDict, memo):
        if idx==len(s):
            return True
        if idx in memo:
            return memo[idx]    
        for i in range(idx, len(s)):
            temp = s[idx: i+1]
            if temp in wordDict and self.solve(i+1, s, wordDict, memo):
                memo[idx] = True
                return True  
        memo[idx] = False
        return False                  