#Approach 1 - Recursion
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else :
            return self.fib(n - 1) + self.fib(n - 2)
        
#Approach 2 - Memoization        
class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                memo[n] = helper(n - 1) + helper(n - 2)
                return memo[n]
        return helper(n)
    
#Approach 3 - Tabulation    
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
#Approach 4 - Space Optimization
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        prev2 = 0
        prev1 = 1

        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1
    