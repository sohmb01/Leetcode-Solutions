# Problem ID: 3309
# Title: Count Prefix and Suffix Pairs I
# Runtime: 11 ms

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(a,b):
            k = len(a)
            if k>len(b):
                return False
            # print(b[])
            
            return a == b[:k] and a == b[-k:]
        cnt = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    cnt+=1
        return cnt