# Problem ID: 1020
# Title: Longest Turbulent Subarray
# Runtime: 99 ms

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curr, best1 = 1, 1
        for i in range(len(arr)-1):
            if i%2 and arr[i]>arr[i+1]:
                curr+=1
            elif i%2==0 and arr[i]<arr[i+1]:
                curr+=1
            else:
                curr = 1
            best1= max(curr,best1)
        curr, best2 = 1, 1
        for i in range(len(arr)-1):
            if i%2 and arr[i]<arr[i+1]:
                curr+=1
            elif i%2==0 and arr[i]>arr[i+1]:
                curr+=1
            else:
                curr = 1
            best2 = max(curr,best2)
        return max(best1,best2)
