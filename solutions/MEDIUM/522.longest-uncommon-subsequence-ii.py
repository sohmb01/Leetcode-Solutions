# Problem ID: 522
# Title: Longest Uncommon Subsequence II
# Runtime: 2 ms

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        def isSubsequence(a,b):
            i = j = 0
            while i< len(a) and j < len(b):
                if a[i] == b[j]:
                    i+=1
                j+=1
            return i == len(a) 

        strs.sort(key= lambda x:len(x), reverse = True)
        
        for i in range(len(strs)):
            flag = True
            for j in range(len(strs)):
                if i!=j and isSubsequence(strs[i],strs[j]):
                    flag = False
                    break
            if flag:
                return len(strs[i])
        return -1
