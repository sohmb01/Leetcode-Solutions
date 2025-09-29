# Problem ID: 905
# Title: Length of Longest Fibonacci Subsequence
# Runtime: 1674 ms

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        res = 2
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                a, b , l = arr[i], arr[j], 2
                while a+b in s:
                    a,b,l = b, a+b, l+1
                res = max(res,l)
        return 0 if res<3 else res