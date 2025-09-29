# Problem ID: 1448
# Title: Maximum 69 Number
# Runtime: 0 ms

class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [x for x in str(num)]
        
        for i in range(len(digits)):
            if digits[i] == "6":
                digits[i] ="9"
                break
       
        return int("".join(digits))
