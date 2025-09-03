class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.helper(0, [], s, result)
        return result

    def helper(self, idx, temp, s, result):
        if idx == len(s):
            result.append(temp[:])
            return
        for i in range(idx, len(s)):
            pal_string = s[idx:i+1]
            if(self.check_pal(pal_string)):
                temp.append(pal_string)
                self.helper(i+1, temp, s, result)
                temp.pop()

    def check_pal(self, pal_str):
        start , end = 0, len(pal_str)-1
        while start<end:
            if pal_str[start] != pal_str[end]:
                return False
            start += 1
            end -= 1
        return True     


# Another approach

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        temp = []
        result = []
        def is_palindrome(l, r):
            return s[l:r+1] == s[l:r+1][::-1]

        def helper(l, r):
            if not is_palindrome(l, r):
                return
            temp.append(s[l:r+1])
            if r == len(s) -1:
                result.append(temp[:])
            else:
                for i in range(r+1, len(s)):
                    helper(r+1, i)
            temp.pop()

        for i in range(0, len(s)):
            helper(0, i)
        return result                    

