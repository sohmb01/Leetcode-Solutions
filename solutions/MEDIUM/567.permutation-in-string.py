# Problem ID: 567
# Title: Permutation in String
# Runtime: 16 ms

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        if len(s2)<windowSize:
            return False
        mp = [0]*26
        target = [0]*26
        getIndex = lambda char : ord(char)-ord('a')
        for i in range(windowSize):
            target[getIndex(s1[i])]+=1
            mp[getIndex(s2[i])]+=1
       
        for i in range(1,len(s2)-windowSize+1):
            if mp==target:
                return True
            
            mp[getIndex(s2[i-1])]-=1
            mp[getIndex(s2[i+windowSize-1])]+=1

        return mp==target
