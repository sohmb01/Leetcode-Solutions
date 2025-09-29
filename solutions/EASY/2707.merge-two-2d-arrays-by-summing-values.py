# Problem ID: 2707
# Title: Merge Two 2D Arrays by Summing Values
# Runtime: 0 ms

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        i,j = 0,0
        l1,l2 = len(nums1),len(nums2)
        ret = []
        while i<l1 and j<l2:
            if nums1[i][0] == nums2[j][0]:
                idx = nums1[i][0]
                val = nums1[i][1] + nums2[j][1]
                i+=1
                j+=1
            elif nums1[i][0] < nums2[j][0]:
                idx = nums1[i][0]
                val = nums1[i][1]
                i+=1
            else:
                idx = nums2[j][0]
                val = nums2[j][1]
                j+=1
            ret.append([idx,val])
        if i==l1:
            ret = ret + nums2[j:]
        else:
            ret = ret + nums1[i:]
        return ret
            

                