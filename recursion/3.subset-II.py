class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.solve(0, [], nums, result)
        return result
    def solve(self, idx, temp,  nums, result):
        result.append(temp[:])    
        for i in range(idx, len(nums)):
            if i>idx and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.solve(i+1, temp, nums, result)  
            temp.pop()