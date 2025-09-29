# Problem ID: 556
# Title: Next Greater Element III
# Runtime: 0 ms

class Solution:
    def nextGreaterElement(self, n: int) -> int:

        def transform(l):
            sl = sorted(l)
            idx = 0
            while idx<len(sl) and sl[idx] <= l[0]:
                idx+=1
            ele = sl.pop(idx)
            return [ele] + sl


        digits = [x for x in str(n)]
        flag = False
        for i in range(len(digits)-2,-1,-1):
            if digits[i] < digits[i+1]:
                digits = digits[:i] + transform(digits[i:])
                flag = True
                break
        
        res = int("".join([str(x) for x in digits]))
        print(res)
        return res if flag and res <= 2**31 - 1 else -1

