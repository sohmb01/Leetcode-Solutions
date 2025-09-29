# Problem ID: 3601
# Title: Find the K-th Character in String Game II
# Runtime: 0 ms

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        ans = 0
        while k != 1:
            t = k.bit_length()-1
            if (1<<t) == k:
                t-=1
            k -= 1<<t
            if operations[t]:
                ans+=1
        return chr(ord('a')+(ans%26))