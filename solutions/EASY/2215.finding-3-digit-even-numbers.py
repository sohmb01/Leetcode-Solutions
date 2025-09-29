# Problem ID: 2215
# Title: Finding 3-Digit Even Numbers
# Runtime: 3274 ms

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j==k or i==k or digits[i]==0:
                        continue
                    num = digits[i]*100 + digits[j]*10 + digits[k]
                    if num%2 == 0:
                        res.add(num)
        return sorted(list(res))