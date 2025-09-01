class Solution:
	def subsetSums(self, arr):
		# code here
		result = []
		self.solve(0, 0, arr, result)
		return result
	def solve(self, idx, sum, arr, result):
		if idx == len(arr):
			result.append(sum)
			return
		self.solve(idx+1, sum+arr[idx], arr, result)
		self.solve(idx+1, sum, arr, result)



		
