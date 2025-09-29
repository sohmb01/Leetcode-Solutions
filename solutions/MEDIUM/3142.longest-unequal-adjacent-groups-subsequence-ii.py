# Problem ID: 3142
# Title: Longest Unequal Adjacent Groups Subsequence II
# Runtime: 755 ms

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        def getHammingDistance(a,b):
            if len(a) != len(b):
                return False
            cnt = 0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    cnt+=1
                if cnt>1:
                    return False
            return True

        @cache
        def getSubsequence(i):
            if i == n-1:
                return [n-1]
            
            ret = []
            for j in range(i+1,n):
                if groups[i] != groups[j] and getHammingDistance(words[i],words[j]):
                    temp = getSubsequence(j)
                    if len(temp) > len(ret):
                        ret = temp 
            return [i] + ret
        
        ans = []
        for i in range(n):
            temp = getSubsequence(i)
            if len(temp) > len(ans):
                ans = temp
        ans = [words[i] for i in ans]
        return ans