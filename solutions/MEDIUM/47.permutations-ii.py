# Problem ID: 47
# Title: Permutations II
# Runtime: 7 ms

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        counter = Counter(nums)
        def backtrack(res):
            if len(res) == n:
                ans.append(res)
                return
            for key in counter:
                if counter[key]:
                    counter[key] -=1
                    backtrack(res + [key])
                    counter[key] +=1
        backtrack([])
        return ans
            
            
