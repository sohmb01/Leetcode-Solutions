# Problem ID: 131
# Title: Palindrome Partitioning
# Runtime: 51 ms

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []
        n = len(s)

        def isPalindrome(s):
            l,r = 0,len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def dfs(i):
            if i >= n:
                ans.append(part[:])
                return
    
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return ans

