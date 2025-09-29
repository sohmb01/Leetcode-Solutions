# Problem ID: 890
# Title: Lemonade Change
# Runtime: 136 ms

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 , c10 = 0,0
        for i in bills:
            change = i - 5
            if change == 0:
                c5+=1
            if change == 5 and c5==0:
                return False
            if change == 5 and c5>0:
                c5-=1
                c10+=1
            if change == 15:
                if c5==0 or (c10==0 and c5<3):
                    return False
                if c10>0:
                    c10-=1
                    c5-=1
                    continue
                else:
                    c5-=3
        return True