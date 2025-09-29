# Problem ID: 2509
# Title: Minimize XOR
# Runtime: 0 ms

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        def getSetBits(num):
            setBits = 0
            while num:
                if num%2:
                    setBits+=1
                num = num >> 1
            return setBits
        
        sb1 = getSetBits(num1)
        sb2 = getSetBits(num2)
        ans = 0
        if sb1 >= sb2:
            i = 0
            cnt = sb1-sb2
            ans = num1
            while cnt:
                if ans%2:
                    num1 = num1 & (num1 - 1)
                    cnt-=1
                ans = ans>>1
                i+=1
            ans = num1
        
        else:
            i=0
            sb2-=sb1
            ans = num1
            while sb2:
                if not num1%2:
                    ans += pow(2,i)
                    sb2-=1
                num1= num1>>1
                i+=1
        return ans
        