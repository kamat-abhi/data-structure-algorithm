from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        n = len(num)
        def solve(idx, expr, value, prev):
            if idx == n and value == target:
                result.append(expr)
                return
            for i in range(idx, n):
                if i>idx and num[idx] == '0':
                    break
                curr_str = num[idx:i+1]
                curr = int(curr_str)

                if idx == 0:
                    solve(i+1, curr_str, curr, curr)
                else:
                    solve(i+1, expr + '+' + curr_str, value+curr, curr)
                    solve(i+1, expr + '-' + curr_str, value-curr, -curr)
                    solve(i+1, expr + '*' + curr_str, value-prev+prev*curr, prev*curr)

        solve(0, "", 0, 0)
        return result          