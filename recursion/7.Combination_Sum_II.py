class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  
        self.solve(candidates, 0, target, [], result)
        return result
    def solve(self, arr, idx, tar, temp, result):
        if tar == 0:
            result.append(temp[:])
            return
        if tar < 0:
            return
        for i in range(idx, len(arr)):
            if i > idx and arr[i] == arr[i-1]:
                continue
            temp.append(arr[i])
            self.solve(arr, i+1, tar-arr[i], temp, result)
            temp.pop()
