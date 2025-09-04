class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []
        if n >= (k*(k+1)//2):
            self.find_combination(0, 1, n, k, [], result)
        return result

    def find_combination(self, sum, idx, n, k, temp, result):
        if len(temp) == k:
            if sum == n:
                result.append(temp[:])
            return
        for i in range(idx, 10):
            if sum+i > n:
                break
            temp.append(i)
            self.find_combination(sum+i, i+1, n, k, temp, result)
            temp.pop()