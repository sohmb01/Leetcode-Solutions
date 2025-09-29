# Problem ID: 2689
# Title: Rearranging Fruits
# Runtime: 93 ms

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        
        freq = Counter(basket1) + Counter(basket2)
        for count in freq.values():
            if count % 2:
                return -1
        
        toSwap = []
        count1 = Counter(basket1)
        for fruit, count in freq.items():
            target = count // 2
            diff = count1.get(fruit, 0) - target 
            for _ in range(abs(diff)):
                toSwap.append(fruit)
        toSwap.sort()

        minVal = min(freq.keys())
        cost = 0
        for i in range(len(toSwap) // 2):
            cost += min(toSwap[i],2 * minVal)
        return cost






