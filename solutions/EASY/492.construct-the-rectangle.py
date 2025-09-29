# Problem ID: 492
# Title: Construct the Rectangle
# Runtime: 1772 ms

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i,j=1,area
        m=area
        while i<=j:
            if area%i == 0:
                j=area//i
                if abs(i-j)<m:
                    m=abs(i-j)
                    l=max(i,j)
                    w=min(i,j)
                
            i+=1
        return [l,w]
            