# Problem ID: 17
# Title: Letter Combinations of a Phone Number
# Runtime: 0 ms

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if not digits:
            return []
        ans = []
        def rec(digits, s):
            if not digits:
                ans.append(s)
                return
            idx = int(digits[0])-2
            for char in l[idx]:
                rec(digits[1:],s+char)
        rec(digits,"")
        return ans
            