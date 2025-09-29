# Problem ID: 943
# Title: Sum of Subarray Minimums
# Runtime: 91 ms

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        l,r = [0]*len(arr),[0]*len(arr)

        for i in range(len(arr)):
            k = i-1
            while k>=0 and arr[i] < arr[k]:
                k = l[k]
            l[i] = k
        
        for i in range(len(arr)-1,-1,-1):
            k = i+1
            while k<len(arr) and arr[i] <= arr[k]:
                k = r[k]
            r[i] = k
        
        res = 0
        for i, num in enumerate(arr):
            res = (res + num * (i-l[i]) * (r[i]-i))%mod
        
        return res

        
