# Problem ID: 3600
# Title: Find the K-th Character in String Game I
# Runtime: 0 ms

class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a') + (k - 1).bit_count())
        