# Problem ID: 940
# Title: Fruit Into Baskets
# Runtime: 183 ms

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitTypes = set()
        l,n = 0,len(fruits)
        res = 0
        freq = defaultdict(int)

        for r in range(n):
            freq[fruits[r]]+=1
            while len(freq) > 2:
                freq[fruits[l]]-=1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l+=1
            res = max(res, r-l+1)
        return res




        