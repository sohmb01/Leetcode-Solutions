# Problem ID: 3462
# Title: Vowels Game in a String
# Runtime: 51 ms

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set(['a','e','i','o','u'])
        cnt = 0
        for c in s:
            if c in vowels:
                cnt+=1
        return cnt!=0