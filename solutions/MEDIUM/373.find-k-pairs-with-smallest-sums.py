# Problem ID: 373
# Title: Find K Pairs with Smallest Sums
# Runtime: 99 ms

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        ans = []
        n1,n2 = len(nums1),len(nums2)
        heap = [(nums1[0]+nums2[0],0,0)]
        visit = set()
        while k and heap:
            s,i,j = heappop(heap)
            ans.append([nums1[i],nums2[j]])
            k-=1
            if j+1<n2 and (i,j+1) not in visit:
                visit.add((i,j+1))
                heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
            if i+1<n1 and (i+1,j) not in visit:
                visit.add((i+1,j))
                heappush(heap,(nums1[i+1]+nums2[j],i+1,j))
        return ans
