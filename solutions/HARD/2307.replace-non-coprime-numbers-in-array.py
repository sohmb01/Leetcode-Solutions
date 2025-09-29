# Problem ID: 2307
# Title: Replace Non-Coprime Numbers in Array
# Runtime: 315 ms

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        def gcd(a,b):
            return a if b == 0 else gcd(b, a % b)
        def lcm(a,b):
            return (a // gcd(a, b)) * b

        ans = []
        curr = nums[0]
        for num in nums[1:]:
            if gcd(curr,num)>1:
                curr = lcm(curr,num)
                while ans and gcd(curr,ans[-1])>1:
                    curr = lcm(curr, ans.pop())
            else:
                ans.append(curr)
                curr = num
        ans.append(curr)
        return ans