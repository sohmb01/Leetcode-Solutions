# Problem ID: 4
# Title: Median of Two Sorted Arrays
# Runtime: 3 ms

class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        na,nb= len(a),len(b)
        if na>nb:
            b,a = a,b
            na,nb= nb,na
        
        half = (na+nb+1)//2
        l,r = 0, na-1
        while True:
            mida = (l+r)//2
            midb = half - mida - 2

            la = a[mida] if mida>=0 else float("-inf")
            ra = a[mida+1] if mida < na-1 else float("inf")
            lb = b[midb] if midb>=0 else float("-inf")
            rb = b[midb+1] if midb < nb-1 else float("inf") 

            if la<=rb and lb<=ra:
                if (na+nb)%2:
                    return max(la,lb)
                return (max(la,lb)+min(ra,rb))/2.0
            elif la > rb:
                r = mida-1
            else:
                l = mida+1
            
                
                
        