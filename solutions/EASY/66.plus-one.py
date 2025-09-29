# Problem ID: 66
# Title: Plus One
# Runtime: 0 ms

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n-1,-1,-1):
            newDigit = ( (digits[i] + carry) % 10 )
            carry = (digits[i]+ carry) // 10
            digits[i] = newDigit
        if carry:
            digits = [1]+digits
        return digits
        