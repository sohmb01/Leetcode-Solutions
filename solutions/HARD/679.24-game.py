# Problem ID: 679
# Title: 24 Game
# Runtime: 65 ms

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        div = lambda x,y : reduce(truediv,(x,y)) if y else inf
        ops = (add, sub, mul, div)

        def dfs(cards):
            if len(cards)<2:
                return isclose(cards[0], 24)
            
            for p in set(permutations(cards)):
                for num in {reduce(op,p[:2]) for op in ops}:
                    if dfs([num] + list(p[2:])):
                        return True
            return False
        return dfs(cards)
        