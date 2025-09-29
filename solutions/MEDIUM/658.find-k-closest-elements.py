# Problem ID: 658
# Title: Find K Closest Elements
# Runtime: 3 ms

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x<= arr[0]:
            return arr[:k]
        if x>arr[-1]:
            return arr[-k:]
        n = len(arr)
        c = n-k
        l,r = 0,n-1
        while c:
            if x-arr[l] <= arr[r]-x:
                r-=1
            else:
                l+=1
            c-=1
        return arr[l:r+1]
