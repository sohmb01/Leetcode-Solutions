# Problem ID: 2665
# Title: Minimum Time to Repair Cars
# Runtime: 1103 ms

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        l,r = 1, ranks[0] * (cars**2)
        
        def canBeRepaired(time):
            carsRepaired = 0
            for rank in ranks:
                carsRepaired += int((time/rank) ** 0.5)
            return carsRepaired >= cars

        while l<r:
            m = (l+r)//2
            if canBeRepaired(m):
                r = m
            else:
                l = m+1
        return l
