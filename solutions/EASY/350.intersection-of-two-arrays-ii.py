# Problem ID: 350
# Title: Intersection of Two Arrays II
# Runtime: 232 ms

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    ans.append(nums1[i])
                    nums1[i]=-1
                    nums2[j]=-2
            
        return ans