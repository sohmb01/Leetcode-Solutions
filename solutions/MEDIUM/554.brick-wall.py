# Problem ID: 554
# Title: Brick Wall
# Runtime: 15 ms

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        n = len(wall)
        freq = {}
        for w in wall:
            prefix = 0
            for brick in w:
                prefix+=brick
                if prefix in freq:
                    freq[prefix]+=1
                else:
                    freq[prefix]=1
        
        highestFreq = 0
        for l,f in list(freq.items()):
            if l!= prefix:
                highestFreq = max(highestFreq,f)
        
        return n-highestFreq
