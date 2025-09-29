# Problem ID: 593
# Title: Valid Square
# Runtime: 2 ms

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def dist(a,b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2
        
        s = set()
        l = [p1,p2,p3,p4]
        for i in range(4):
            for j in range(i+1,4):
                d = dist(l[i],l[j])
                if not d:
                    return False
                s.add(d)
        return len(s) == 2