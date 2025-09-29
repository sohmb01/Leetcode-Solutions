# Problem ID: 3657
# Title: Check if Grid can be Cut into Sections
# Runtime: 555 ms

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        rectangles.sort(key = lambda l : l[0])
        print(rectangles)
        cnt = 0
        last = rectangles[0][2]
        i = 1
        while i < len(rectangles):
            start,_,end,_ = rectangles[i]
            if start >= last:
                cnt+=1
            last = max(last,end)
            i+=1
        if cnt >= 2:
            return True

        rectangles.sort(key = lambda l : l[1])
        print(rectangles)
        cnt = 0
        last = rectangles[0][3]
        i = 1
        while i < len(rectangles):
            _,start,_,end = rectangles[i]
            if start >= last:
                cnt+=1
            last = max(last,end)
            i+=1
        if cnt >= 2:
            return True
        
        return False