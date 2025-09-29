# Problem ID: 229
# Title: Majority Element II
# Runtime: 7 ms

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = cnt2 = majEle1 = majEle2 = 0
        n = len(nums)
        for num in nums:
            if num == majEle1:
                cnt1+=1
            elif num == majEle2:
                cnt2+=1
            elif cnt1 == 0:
                majEle1 = num
                cnt1+=1
            elif cnt2 == 0:
                majEle2 = num
                cnt2+=1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1,cnt2 = 0,0
        for num in nums:
            if num == majEle1:
                cnt1+=1
            if num == majEle2:
                cnt2+=1
        ans = []
        if cnt1 > n//3:
            ans.append(majEle1)
        if cnt2 > n//3 and majEle1!=majEle2:
            ans.append(majEle2)
        return ans
