# Problem ID: 28
# Title: Find the Index of the First Occurrence in a String
# Runtime: 16 ms

class Solution(object):
    def strStr(self, haystack, needle):
        if needle=="":
            return 0
        if len(needle)>len(haystack) or needle not in haystack:
            return -1
        hay=len(haystack)
        need=len(needle)
        for i in range (hay-need+1):
            if haystack[i]==needle[0]:
                k=0
                while (k<len(needle) and haystack[i+k]==needle[k]):
                    k+=1
                if k==len(needle):
                    return i
                else :
                    i+=k
        
        