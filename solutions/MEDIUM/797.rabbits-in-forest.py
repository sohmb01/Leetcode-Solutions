# Problem ID: 797
# Title: Rabbits in Forest
# Runtime: 1 ms

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0 
        mp = {}
        for num in answers:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] +=1
        for key, val in mp.items():
            if key == 0:
                res += val
            else:
                res += (val//(key+1))*(key+1)
                if val % (key+1):
                    res += key+1

        return res