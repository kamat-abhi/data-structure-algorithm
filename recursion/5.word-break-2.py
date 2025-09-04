class Solution:
    def wordBreak(self, dict, s):
        # code here
        my_set = set(dict)
        result = []
        self.solve(0, my_set, s, [], result)
        return [" ".join(words) for words in result]
    
    def solve(self, idx, my_set, s, temp, result):
        if idx == len(s):
            result.append(temp[:])
            return
        for i in range(idx, len(s)):
            word = s[idx:i+1]
            if word in my_set:
                temp.append(word)
                self.solve(i+1, my_set, s, temp, result)
                temp.pop()